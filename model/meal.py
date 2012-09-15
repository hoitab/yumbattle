'''
Created on 15 Sep 2012

@author: hoi
'''
from google.appengine.ext import db
from google.appengine.ext import blobstore

class Meal(db.Model):
    picture = blobstore.BlobReferenceProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)
    canteenlocation = db.GeoPtProperty()
    canteenid = db.StringProperty()
    canteenname = db.StringProperty()
    contestcount = db.IntegerProperty()
    contestscore = db.IntegerProperty()
