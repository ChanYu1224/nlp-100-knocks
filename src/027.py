import re

text_file = open('../data/england.txt')
text = text_file.read()
text_file.close()

def retrieve_basic_informations(text):
    """基礎情報の抜き出し"""
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    information_text = re.findall(pattern, text, re.MULTILINE + re.DOTALL)[0]

    pattern = r'^\|(.+?)\s*=\s*(.+?)$'
    informations = dict(re.findall(pattern, information_text, re.MULTILINE + re.DOTALL))

    return informations

def fix_style(text):
    fixed = re.sub(r'\'{2,5}', '', text)
    fixed = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', fixed)
    return fixed

def print_dict(dict):
    for key, value in dict.items():
        print(key +': '+ fix_style(value))

informations = retrieve_basic_informations(text)

print_dict(informations)