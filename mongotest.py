import pymongo

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.xcp92.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database['sudh']

sel_data = collection.find({"courseOffered": {"$gt" : "C"}})

for i in sel_data:
    print(i)

