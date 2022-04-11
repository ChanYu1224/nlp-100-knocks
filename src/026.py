import re

text_file = open('../data/england.txt')
text = text_file.read()
text_file.close()

emphasized_words = re.findall(r'\'{2,4}.+?\'{2,4}', text, re.MULTILINE | re.DOTALL)
words = re.findall(r'\'{2,4}(.+?)\'{2,4}', text, re.MULTILINE | re.DOTALL)

for emphasized_word, word in zip(emphasized_words, words):
    text = text.replace(emphasized_word, word)

print(text)