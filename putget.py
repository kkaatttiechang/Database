#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://katiechang:data@127.0.0.1')
#mongodb://10.34.33.28:33333
#mongodb://katiechang:data@127.0.0.1
db = client.database
quickacc = db.quickacc

class lists:

    @staticmethod
    def put(keyword, num, list1):
        db.quickacc.insert({"keyword":keyword, "int":num, "list": list1})

    @staticmethod
    def get (keyword):
        print db.quickacc.count({'keyword':keyword})
        if db.quickacc.count({'keyword':keyword}) > 0:
            data = quickacc.find_one({'keyword':keyword}, {"keyword": 0, "_id": 0 } )
            return data
        else:
            return ([-1], [-1])

#sample fetch---------------------------------------------------        
letter = ["hi", "ohiyo", "nihao"]
number = [1, 3, 5]
x = lists()
x.put("try", number, letter)
print(x.get("try"))
