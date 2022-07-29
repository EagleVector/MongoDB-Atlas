import pymongo
import pandas as pd
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.xcp92.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['assignment']
collection = database['Dress Sales']

df = pd.read_csv('Dress Sales.xlsx - Sheet1.csv')

dresssalesdata = df.to_dict(orient = 'records')

collection.insert_many(dresssalesdata)
