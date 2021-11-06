from pathlib import Path
import json


#Functions for read and writing

def read_file(file):
    with open(file) as fileObj:
        data = json.load(fileObj)
        return data

def write_file(file,data):
    with open(file, 'w') as fileObj:
        json.dump(data, fileObj)