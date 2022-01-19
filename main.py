import os

from dotenv import load_dotenv

from phase1.db_connector import DBConnector

load_dotenv(".env")
if __name__ == "__main__":
    user_choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")

    conn = DBConnector.Instance(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )