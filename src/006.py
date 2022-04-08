def replace_marks(sentense:str, marks:list) -> str:
  """sentenseからmarks内の記号を全て除去する"""
  for mark in marks:
    sentense = sentense.replace(mark, '')
  return sentense

def retrieve_words_list(sentense:str) -> list:
  """文章から単語のみを抽出する"""
  sentense = replace_marks(sentense, ['.', ',', '?', '!'])
  words = sentense.split(' ')
  return words

def n_gram_char(sentense:str, n:int) -> list:
  """文字単位n-gramを作る"""
  n_gram = []
  for i in range(len(sentense)-(n-1)):
    n_gram.append(sentense[i:i+n])
  return n_gram

def n_gram_word(sentense: str, n:int) -> list:
  """単語単位n-gramを作る"""
  words = retrieve_words_list(sentense)
  n_gram = []
  for i in range(len(words)):
    n_gram.append(words[i:i+n])
  return n_gram

word_1 = "paraparaparadise"
word_2 = "paragraph"

x = n_gram_char(word_1, 2)
y = n_gram_char(word_2, 2)

x = set(x)
y = set(y)

union = x | y
intersection = x & y
difference = x - y

print('union        : ', union)
print('intersection : ', intersection)
print('defference   : ', difference)