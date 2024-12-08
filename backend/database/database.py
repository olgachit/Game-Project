import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()
class Database:
    def __init__(self):
        self.host = os.getenv('HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_DATABASE')
        self.charset = "utf8mb4"
        self.collation = "utf8mb4_general_ci"
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset=self.charset,
                collation=self.collation
            )
            print("Database connection successful")
        except mysql.connector.Error as err:
            print(f"Error connecting to database: {err}")
            self.connection = None

    def cursor(self, **kwargs):
        if self.connection is None:
            raise Exception("Database not connected. Call the connect() method first.")
        return self.connection.cursor();

db = Database()
db.connect()
cur = db.cursor(dictionary=True)
