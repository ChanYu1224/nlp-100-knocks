def replace_marks(sentense:str, marks:list):
  """sentenseからmarks内の記号を全て除去する"""
  for mark in marks:
    sentense = sentense.replace(mark, '')
  return sentense

def retrieve_words_list(sentense:str):
  """文章から単語のみを抽出する"""
  sentense = replace_marks(sentense, ['.', ',', '?', '!'])
  words = sentense.split(' ')
  return words

sentense = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = retrieve_words_list(sentense)

retrieve_indexes = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}
for i in retrieve_indexes:
  char = words[i-1][0] if i == 1 else words[i-1][0:2]
  ans[char] = i

print(ans)