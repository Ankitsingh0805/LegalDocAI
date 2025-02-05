import uuid

def generate_uuid7():
  return str(uuid.uuid4())[:7]


def generate_otp():
    random_number = uuid.uuid4().int
    otp = str(random_number)[-5:]
    return otp

# verification email sender :

from django.core.mail import send_mail

def send_verification_email(to_email, otp):
    subject = "email verification"
    message = f"your email verification OTP is {otp}"
    from_email = 'adityamadwal@gmail.com'
    try:
        send_mail(
            subject,
            message,
            from_email,
            [to_email],
            fail_silently=False,
        )
        return "success"
    except Exception as e:
        return e