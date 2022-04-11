import re

text_file = open('../data/england.txt')
content = text_file.read()
text_file.close()

#基礎情報記述部分の抜き出し
pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
information_content = re.findall(pattern, content, re.MULTILINE + re.DOTALL)[0]

pattern = r'^\|(.+?)\s*=\s*(.+?)$'
informations = dict(re.findall(pattern, information_content, re.MULTILINE + re.DOTALL))

for key, value in informations.items():
    print(key +': '+ value)