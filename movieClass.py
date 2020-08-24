from datetime import datetime
from pymongo import MongoClient


class MoviesClass:
    conn = MongoClient("mongodb://localhost:27017/")

    def add_record(self, new_data):
        pass

    def search(self, mycol):
       pass

    def fetch_records(self, mycol):
        pass


