import re

text_read = open('../data/england.txt')

for line in text_read:
    line = line.replace('\n', '')

    if re.match(r'\[\[ファイル:.+?\|', line):
        media_name = re.match(r'\[\[ファイル:(.+?)\|', line).group(1)
        print(media_name)