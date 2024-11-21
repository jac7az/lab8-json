#!/usr/bin/python3

import json

with open('../data/schacon.repos.json', 'r') as file:
    data = json.load(file)
with open('chacon.csv','a') as chacon:
    for result in data[:5]:
       chacon.write(result['name']+", "+result['html_url']+", "+result['updated_at']+", "+result['visibility']+'\n')
file.close()
