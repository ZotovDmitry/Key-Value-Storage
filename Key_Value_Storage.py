import json
import sys
import argparse
import os
import tempfile
from collections import defaultdict
parser = argparse.ArgumentParser() 


parser.add_argument("-k", "--key")
parser.add_argument("-v", "--val")

args = parser.parse_args() # reading of input
json_data = defaultdict(list)
data = defaultdict(list)
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

directory = str(tempfile.gettempdir()) #temporary file directory
tempfiledir = directory + "/storage.data"
if os.path.exists(tempfiledir) != True: # check if a file exists
    with open(tempfiledir, 'w') as f:
        json.dump(data, f)
if args.key != None and args.val != None:
    with open(tempfiledir, 'r') as f:
        json_data = json.load(f)
    if args.key not in json_data:
        json_data[args.key] = [] # check if dict includes a key
    json_data[args.key].append(args.val)
    with open(tempfiledir, 'w') as f:
        json.dump(json_data, f)
elif args.key != None and args.val == None:
    with open(tempfiledir, 'r') as f:
        json_data = json.load(f)  
    if args.key not in json_data:
        exit()
    out = str(json_data[args.key])
    out = out.replace("'",'')
    out = out.replace("[",'')
    out = out.replace("]",'')
    print(out)
