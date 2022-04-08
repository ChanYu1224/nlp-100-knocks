def cipher(sentense:str) -> str:
  """英小文字ならば(219-文字コード)，そのほかの文字はそのまま出力する"""
  sentense = list(sentense)
  for i, char in enumerate(sentense):
    if ord('a') <= ord(char) <= ord('z'):
      sentense[i] = chr(219-ord(char))
  return "".join(sentense)

sentense = input()
print(cipher(sentense))