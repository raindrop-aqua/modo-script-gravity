# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Author(db.Model):
    name = db.StringProperty()
    twitter = db.StringProperty()
    mail_address = db.EmailProperty()
    mail_notify = db.BooleanProperty(default = False)
    created = db.DateTimeProperty(auto_now_add = True)
    updated = db.DateTimeProperty(auto_now = True)

class AssetObject(db.Model):
    name = db.StringProperty()
    author = db.ReferenceProperty(Author)
    url = db.LinkProperty()
    version = db.StringProperty(default = "0.0")
    rating = db.RatingProperty(default = 0)
    description = db.StringProperty(multiline = True)
    created = db.DateTimeProperty(auto_now_add = True)
    updated = db.DateTimeProperty(auto_now = True)
    categories = db.StringListProperty()

