import re

text_read =  open('../data/england.txt', 'r')

for text in text_read:
    if re.match(r'^\[\[Category:.+\]\]$', text):
        print(text.replace('\n', ''))
