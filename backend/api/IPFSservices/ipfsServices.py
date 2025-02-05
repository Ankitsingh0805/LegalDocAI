import requests
import os
from dotenv import load_dotenv
from typing import Optional, Dict, Any

# Load environment variables
load_dotenv()

class IPFSService:
    def __init__(self):
        """
        Initialize the IPFSService with Pinata credentials.
        Uses JWT for authentication and a custom gateway.
        """
        self.pinata_jwt = os.getenv('PINATA_JWT')
        self.base_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
        self.gateway_url = "https://cyan-advanced-boar-241.mypinata.cloud/ipfs"

        if not self.pinata_jwt:
            raise ValueError("Missing PINATA_JWT in environment variables.")

        self.headers = {
            "Authorization": f"Bearer {self.pinata_jwt}"
        }

    def upload_file(self, file, filename: str) -> Optional[str]:
        """
        Upload a file to Pinata's IPFS storage.

        Args:
            file: In-memory uploaded file from request.FILES.
            filename (str): Custom filename for Pinata.

        Returns:
            str: CID (IpfsHash) if successful, None otherwise.
        """
        try:
            # Read the file and prepare it for upload
            files = {
                "file": (filename, file.read(), file.content_type)
            }

            # Send POST request to Pinata
            response = requests.post(self.base_url, headers=self.headers, files=files)
            response.raise_for_status()

            # Parse response
            json_response = response.json()
            cid = json_response.get("IpfsHash")

            if cid:
                print(f"File uploaded successfully! CID: {cid}")
                return cid
            else:
                print("No IPFS hash returned in the response.")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error uploading file to Pinata: {e}")
            return None

    def get_file_url(self, ipfs_hash: str) -> str:
        """
        Construct the public URL of a file using the custom Pinata gateway.

        Args:
            ipfs_hash (str): The IPFS CID.

        Returns:
            str: Direct URL to access the file.
        """
        return f"{self.gateway_url}/{ipfs_hash}"

    def delete_file(self, ipfs_hash: str) -> bool:
        """
        Remove a file from Pinata (Unpin by CID).

        Args:
            ipfs_hash (str): The IPFS CID to unpin.

        Returns:
            bool: True if successful, False otherwise.
        """
        delete_url = f"https://api.pinata.cloud/pinning/unpin/{ipfs_hash}"

        try:
            response = requests.delete(delete_url, headers=self.headers)
            response.raise_for_status()
            print(f"File {ipfs_hash} successfully removed from Pinata.")
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error deleting file from IPFS: {e}")
            return False

    def get_file_metadata(self, ipfs_hash: str) -> Dict[str, Any]:
        """
        Fetch metadata of a pinned file.

        Args:
            ipfs_hash (str): The IPFS CID.

        Returns:
            Dict[str, Any]: Metadata of the file.
        """
        metadata_url = "https://api.pinata.cloud/data/pinList"
        params = {"hashContains": ipfs_hash}

        try:
            response = requests.get(metadata_url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve file metadata: {e}")
