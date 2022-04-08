word = "パタトクカシーー"
ans = ""

for i in range(len(word)):
  if i%2 == 0:
    ans += word[i]

print(ans)