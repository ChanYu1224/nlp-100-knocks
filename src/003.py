sentense = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
sentense = sentense.replace(',', '')
sentense = sentense.replace('.', '')
words = sentense.split(' ')

counts = []
for word in words:
  counts.append(len(word))

print(counts)