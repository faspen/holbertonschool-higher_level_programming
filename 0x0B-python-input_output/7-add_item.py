#!/usr/bin/python3
""" Module that loads, adds, and saves """
import os
from sys import argv


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg_list = []

if os.path.exists("add_item.json"):
    arg_list = load_from_json_file("add_item.json")
save_to_json_file(arg_list + argv[1:], "add_item.json")
