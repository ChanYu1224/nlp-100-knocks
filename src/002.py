word_1 = "パトカー"
word_2 = "タクシー"

ans = []

for char_1, char_2 in zip(word_1, word_2):
  ans.append(char_1)
  ans.append(char_2)

print("".join(ans))