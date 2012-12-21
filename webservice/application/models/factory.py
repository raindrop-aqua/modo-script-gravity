# -*- coding: utf-8 -*-

from models import AssetObject
import utils

class ListFactory():
    def get(self, categories):
        pass

    def _get_from_datastore(self, categories):
        pass

    def _get_from_memcache(self, categories):
        pass

class DetailFactory():
    def get(self, id):
        pass

    def _get_from_datastore(self, id):
        obj = AssetObject.get_by_id(long(id))
        return utils.to_dict(obj)

    def _get_from_memcache(self, id):
        pass

    def _put_to_memcache(self, id, body):
        pass

