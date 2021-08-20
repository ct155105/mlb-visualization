from pymongo import MongoClient

client = MongoClient('mongo-db')

db = client.poc 

collection = db.hello_world

# post_id = collection.insert_one({'label': 'Hello World from Docker!'}).inserted_id

for c in collection.find():
    print(c)