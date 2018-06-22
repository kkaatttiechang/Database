#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://10.34.33.28:33333')
db = client.database
quickacc = db.quickacc

class lists:
    keyword = []
    link = []
    def put(self):
        for element in range(len(self.keyword)):
            tag = self.keyword[element]
            url = self.link[element]
            db.quickacc.insert({"keyword": tag, "link": url})
	    print ({"keyword": tag, "link": url})

    def get(self,keyword):
        if db.quickacc.count({'keyword':keyword}) > 0:
            data = quickacc.find_one({'keyword':keyword})
            return data
        else:
            return ([-1], [-1])

#sample fetch---------------------------------------------------        
letter = ["hi", "ohiyo", "nihao"]
number = [1, 3, 5]
x = lists()
x.keyword = number
x.link = letter
print (x.get(5))
