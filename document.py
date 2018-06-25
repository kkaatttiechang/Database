#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId
import cv2



global tublelist

class profile:
    client = MongoClient('mongodb://10.34.33.28:33333')
    db = client.database
    crawl = db.crawl
    imagepath = ""
    source = ""
    web_url = ""
    image_url = ""
    datetime = 0
    keyword =  ""
    tag = ""
    change = ""
    

    def create (self):
        prev_id = self.db.crawl.count()
        documentformatter={
            "source":self.source,
            "web url": self.web_url,
            "image url":self.image_url,
            "keyword":self.keyword,
            "height":self.imagepath.shape[0],
            "width":self.imagepath.shape[1],
            "datetime": self.datetime,
            "_id" : ObjectId(repr(prev_id+1))
        }
        self.db.crawl.insert([documentformatter])

    def find_bykeyword (self, tags):
        count = self.db.crawl.find({"keyword":{"$all":tags}}).count()
        if count  > 0:
            for users in count:
                self.profilelist[self.user] = self.db.crawl.find_one({"keyword":{"$all":tags}}).skip(self.user)
            tuplelist = tuple(self.profilelist)
            return self.db.crawl.find({"keyword":{"$all":tags}}).count()
        else:
            return -1

    def update(self, tag, change):
        numupdates = self.find_bykeyword(tag)
        if numupdates > 0:
            self.db.collection.update({"keyword":tag},{"keyword":change} )
#update keywords

    def delete(self, tag):
        numdeletes = self.find_bykeyword(tag)
        if numdeletes > 0:
            self.db.collection.remove({"keyword":tag})

test = profile()
test.imagepath = print("\home\katiechang\Documents\\")


        
