import os

from dotenv import load_dotenv

from phase12 import auth
from phase12.db_connector import DBConnector
from phase12.email_service import EmailService
from phase12.repository import UserRepository
from phase3.menu import phase3Menu

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
    while user_choice != 3:
        user_choice = int(
            input(
                "Choose from the list below: \n"
                "1. Sign up.\n"
                "2. Sign in.\n"
                "3. Quit.\n"
            )
        )
        if user_choice == 1:
            auth.sign_up(user_repo=user_repo)
            print()
        elif user_choice == 2:
            login_result = auth.login(user_repo=user_repo)
            if login_result is True:
                while 1:
                    phase3Menu()
                    print()