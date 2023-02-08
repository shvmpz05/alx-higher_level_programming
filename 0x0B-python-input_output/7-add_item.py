#!/usr/bin/python3
"""Import json"""


import sys
import json
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    jsonlist = load_from_json_file("add_item.json")
except:
    jsonlist = []


for i in sys.argv[1:]:
    jsonlist.append(i)

save_to_json(jsonlist, "add_item.json")
