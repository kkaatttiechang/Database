#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId
import cv2





class profile:
    def __init__(self,server=''):
        if server =='':
            self.client = MongoClient('mongodb://10.34.33.28:33333')
        else:
            self.client =MongoClient(server)
        self.db = self.client.database
        self.profilelist =[]




    def create (self,imagepath, source, web_url, image_url, datetime, keyword):
        prev_id = self.db.crawl.count()

        documentformatter={
            "source":source,
            "web url": web_url,
            "image url":image_url,
            "keyword":keyword,
            "height":imagepath.shape[0],
            "width":imagepath.shape[1],
            "datetime": datetime,
            "_id" : ObjectId(repr(prev_id+1))
        }
        self.db.crawl.insert([documentformatter])


    def find_bykeyword (self,tags):
        count = self.db.crawl.find({"keyword":{"$all":tags}}).count()
        if count  > 0:
            for users in count:
                self.profilelist[users] = self.db.crawl.find_one({"keyword":{"$all":tags}}).skip(users)
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

<<<<<<< HEAD
=======
test = profile()
test.imagepath = print("\home\katiechang\Documents\\")

>>>>>>> 401d6dae70efd93a0ee7b9ebd82368b7c3c1d216

        
