# -*- coding: utf-8 -*-

import datetime, time
from google.appengine.ext import db

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

def to_dict(obj):
    output = {}
    output["id"] = obj.key().id()
    for key, prop in obj.properties().iteritems():
        value = getattr(obj, key)

        if value is None or isinstance(value, SIMPLE_TYPES):
            output[key] = value
        elif isinstance(value, datetime.date):
            # Convert date/datetime to ms-since-epoch ("new Date()").
            ms = time.mktime(value.utctimetuple())
            ms += getattr(value, 'microseconds', 0) / 1000
            output[key] = int(ms)
        elif isinstance(value, db.GeoPt):
            output[key] = {'lat': value.lat, 'lon': value.lon}
        elif isinstance(value, db.Model):
            output[key] = to_dict(value)
        else:
            raise ValueError('cannot encode ' + repr(prop))
    return output
