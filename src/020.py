import json

json_open = open('../data/jawiki-country.json', 'r')

while True:
    json_load = json.loads(json_open.readline())
    if json_load['title'] == 'イギリス':
        print(json_load['text'])
        break

text_open = open('../data/england.txt', 'w')
text_open.write(json_load['text'])