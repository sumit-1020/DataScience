import pymongo
client = pymongo.MongoClient("mongodb+srv://SumitRaj:9934287065@sumit.3lmjqsc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    'name':'Sumit',
    'email':'sumitraj1020@gmail.com',
    'surname':'Raj'
}

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)