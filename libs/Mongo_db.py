from pymongo import MongoClient

MONGODB_URL = "mongodb://localhost:27017/"

class MongoDB:
    def __init__(self,db_name):
        self.db_name = db_name
    def __enter__(self):
        self.client = MongoClient(MONGODB_URL)
        self.db = self.client[self.db_name]
        return self.db
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
    def __del__(self):
        self.client.close()
