# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from google.appengine.ext import db
from application.models.models import Author, AssetObject
import application.services as service

app = Flask(__name__)

@app.route("/")
def list():
    return jsonify(service.get_asset_list([]))

@app.route("/d/<int:id>")
def detail(id):
    return jsonify(service.get_asset_detail(id))

@app.route("/add")
def add():
    author = Author.get_by_id(long(13))
#    author.name = u"渥美政廣"
#    author.mail_address = "abc.xyz@gmail.com"
#    author.put()

    script = AssetObject()
    script.name = "window settings script 2"
    script.author = author
    script.url = "http://www.lux.com/script/001/files.zip"
    script.version = "1.0"
    script.rating = db.Rating("50")
    script.description = u"このスクリプトは\n曲線を描画するスクリプトです。"
    script.categories = ["circle", "modo", "script"]
    script.put()
    return "OK!"

if __name__ == "__main__":
    app.run()