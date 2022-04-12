import re
import requests

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
    """データの整形"""
    # 強調の除去
    fixed = re.sub(r'\'{2,5}', '', text)
    # 内部リンクの除去
    fixed = re.sub(r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]', r'\1', fixed)
    # 外部リンクの除去
    fixed = re.sub(r'https?://[\w!?/\+\-_~=;\.,*&@#$%\(\)\'\[\]]+', '', fixed)
    # HTMLタグの除去
    fixed = re.sub(r'<.+?>', '', fixed)
    #テンプレートの除去
    fixed = re.sub(r'\{\{.*?\}\}', '', fixed)
    #ファイル名の取り出し
    fixed = re.sub(r'\[\[ファイル:(.+?)\|.*?\]\]', r'\1', fixed)
    return fixed

def fix_dict_value(dict:dict):
    for key, value in dict.items():
        dict[key] = fix_style(value)
    return dict

def print_dict(dict):
    for key, value in dict.items():
        print(key +': '+ value)

 
informations = retrieve_basic_informations(text)
informations = fix_dict_value(informations)

file = 'File:'+ informations['国旗画像'].replace(' ', '_')
url = 'https://commons.wikimedia.org/w/api.php'
params = {
    'action': 'query',
    'titles': file,
    'prop': 'imageinfo',
    'format': 'json',
    'iiprop': 'url',
}

response = requests.get(url=url, params=params)
image_url = re.findall(r'\"url\"\:\"(.+?)\"', response.text)[0]

print(image_url)