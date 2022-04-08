from random import shuffle

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

def shuffle_char(word:str) -> str:
  """両端の文字以外をシャッフルする"""
  if len(word) <= 4:
    return word

  start = word[0]
  end = word[-1]
  center = list(word[1:len(word)-1])
  shuffle(center)
  center = "".join(center)
  result = start + center + end
  
  return result

sentense = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."
words = retrieve_words_list(sentense)
ans = []
for word in words:
  ans.append(shuffle_char(word))

ans = " ".join(ans)
print(ans)