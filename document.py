#!/usr/bin/python

from pymongo import MongoClient
from bson import ObjectId
import cv2

client = MongoClient('mongodb://10.34.33.28:33333')
db = client.database
crawl = db.crawl

global profilelist[]


class profile:

    @staticmethod
    def create (imagepath, source, web_url, image_url, datetime, keyword):
        prev_id = db.crawl.count()
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
        db.crawl.insert([documentformatter])

    @staticmethod
    def find_bykeyword (tags):
        count = db.crawl.find({"keyword":{"$all":tags}}).count()
        if count  > 0:
            for users in count:
                profilelist[user] = db.crawl.find_one({"keyword":{"$all":tags}}).skip(user)
            return db.crawl.find({"keyword":{"$all":tags}}).count()
        else:
            return -1

    @staticmethod
    def update(tag, change):
        numupdates = find_bykeyword(tag)
        if numupdates > 0:
            db.collection.update({"keyword":tag},{"keyword":change} )
#update keywords

    @staticmethod
    def delete(self, tag):
        numdeletes = find_bykeyword(tag)
        if numdeletes > 0:
            db.collection.remove({"keyword":tag})


        
