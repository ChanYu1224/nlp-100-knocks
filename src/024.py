import re

text_read = open('../data/england.txt')

for line in text_read:
    line = line.replace('\n', '')
    media_name = re.match(r'\[\[ファイル:')