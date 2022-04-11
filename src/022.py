import re

text_read = open('../data/england.txt')

category_lines = []
for text in text_read:
    if re.match(r'^\[\[Category:.+\]\]$', text):
        category_lines.append(text.replace('\n', ''))

text_read.close()

for category_line in category_lines:
    category = re.findall(r'^\[\[Category:(.+)\]\]$', category_line)
    print(category[0].split('|')[0])
    