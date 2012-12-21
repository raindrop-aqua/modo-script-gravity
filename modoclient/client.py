# -*- coding: utf-8 -*-

import urllib2
import json


def main():
    pagehandle = urllib2.urlopen("http://localhost:8080/")
    json_contents =  pagehandle.read()
    contents = json.loads(json_contents)
    print "ok!"

if __name__ == "__main__":
    main()
