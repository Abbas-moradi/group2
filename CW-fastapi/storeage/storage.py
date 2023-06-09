from pymongo import MongoClient


client = MongoClient(host="localhost", port=27017, connect=True)
db = client["library"]
collection_book = db["book"]
collection_user = db["user"]

Session = dict()
