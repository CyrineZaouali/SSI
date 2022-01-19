import os

from dotenv import load_dotenv

from phase12 import auth
from phase12.db_connector import DBConnector
from phase12.email_service import EmailService
from phase12.repository import UserRepository

load_dotenv(".env")
if __name__ == "__main__":
    user_choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")
    EMAIL_LOGIN: str = os.environ.get("EMAIL_LOGIN")
    EMAIL_PASSWORD: str = os.environ.get("EMAIL_PASSWORD")
    conn = DBConnector.Instance(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )
    email_service = EmailService(
        sender_email=EMAIL_LOGIN, sender_password=EMAIL_PASSWORD
    )
    user_repo = UserRepository(db_connector=conn, email_service=email_service)
    while user_choice != 4:
        user_choice = int(
            input(
                "Choose from the list below: \n"
                "1. Signup.\n"
                "2. Signin.\n"
                "4. Quit.\n"
            )
        )
        if user_choice == 1:
            auth.sign_up(user_repo=user_repo)
            print()
            print()
        elif user_choice == 2:
            auth.login(user_repo=user_repo)
            print()
            print()