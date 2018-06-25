#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId



class servdictionary:


    def __init__(self,server=""):
        if server == "":
            self.client = MongoClient('mongodb://10.34.33.28:33333')
        else:
            self.client= MongoClient(server)
        self.db = self.client.database
        self.quickacc = self.db.quickacc


  
    def put(self,keyword, num, list1):
        self.db.quickacc.insert({"keyword":keyword, "int":num, "list": list1})


    def get(self,keyword):
        if self.db.quickacc.count({'keyword':keyword}) > 0:
            data = self.quickacc.find_one({'keyword':keyword}, {"keyword": 0, "_id": 0 } )
            return data
        else:
            return

#sample fetch---------------------------------------------------        
# letter = ["hi", "ohiyo", "nihao"]
# number = [1, 3, 5]
# x = servdictionary()
# x.put("try", number, letter)
# print(x.get("try").get('list'))
