# AI-Powered Legal Documentation assistant (LegalDocAI)

The legal industry is heavily reliant on documents, from contracts to legal briefs. Manually drafting, analysing, and securely storing these documents is time-consuming and prone to human error. LegalDocAI addresses this by leveraging artificial intelligence for document creation and analysis while utilizing IPFS (Inter Planetary File System) for tamper-proof storage.

## Project Overview

Legal professionals face a major challenge in summarizing extensive legal documents, leading to inefficiencies in the legal process. This project implements AI technologies for two primary purposes:

1. **Legal Document Summarization**: Automating the summarization of complex legal documents using BART (for extractive summarization) and PEGASUS (for abstractive summarization).
2. **Legal Document Management**: Utilizing AI for the efficient organization, retrieval, and summarization of legal texts to aid professionals in case preparation.

# Primary Objectives:

1. Automate the process of legal document creation and analysis.
2. Ensure secure and decentralized storage of documents using IPFS.
3. Provide a user-friendly interface for legal professionals to manage and analyze documents effectively.

## Methodology

The workflow of the project is outlined below:

1. **Document Collection**: Legal documents are collected from public sources such as SCI, IndianKanoon, and Manupatra.
2. **Text Extraction**: Using Optical Character Recognition (OCR) techniques to extract raw text from legal documents.
3. **Text Normalization**: Legal abbreviations are expanded, and sections/articles are appended with summaries for clarity.
4. **Summarization & Evaluation**: The model outputs are evaluated based on Open AI API and NLP.

## Future Work

- Improve Project models for better abstractive summarization results and real-time suggestions
- Implement this summarization technique for other complex legal documents.

## References

1. Ghosh, S., Dutta, M., & Das, T. (2022). _Indian Legal Text Summarization: A Text Normalisation-based Approach_. 2022 IEEE 19th India Council International Conference (INDICON). [Link](https://github.com/SATYAJIT1910/ILDS).

2. Meena, K., Tanusha, G., Renuka, G., Saraswathi, K., & Anuradha, S. (2024). _Enhancing Legal Document Management Efficiency: An AI-Powered Solution Addressing Interpretation Challenges_. Journal of Engineering and Technology Management, 72, 650-662.
