from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:test123!@cluster0.yz1ahxw.mongodb.net/?retryWrites=true&w=majority")


db = client.todo_db

collection_name = db["todo_collection"]