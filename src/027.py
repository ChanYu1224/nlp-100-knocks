import re

text_file = open('../data/england.txt')
text = text_file.read()
text_file.close()

links = re.findall(r'\[\[.+?\]\]', text, re.MULTILINE | re.DOTALL)
links_text = re.findall(r'\[\[(.+?)\]\]', text, re.MULTILINE | re.DOTALL)

print(links_text)