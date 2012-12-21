# -*- coding: utf-8 -*-

from google.appengine.ext import db
from models.models import AssetObject
import models.utils

def get_asset_list(categories):
    objects = AssetObject.all().order("-updated").fetch(100, 0)
    result = [models.utils.to_dict(obj) for obj in objects]
    return dict(data = result)

def get_asset_detail(id):
    obj = AssetObject.get_by_id(long(id))
    return models.utils.to_dict(obj)
