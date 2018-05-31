#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import MySQLdb


dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

jsonstr = json.dumps(dict,sort_keys=True, indent=4, separators=(',', ': '))
print(dict)
print(jsonstr)
