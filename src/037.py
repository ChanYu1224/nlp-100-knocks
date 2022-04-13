import collections
import matplotlib.pyplot as plt

mecab_file = open('../data/neko.txt.mecab', 'r')

sentences = []
morphs = []
for line in mecab_file:
    if line != 'EOS\n':
        fields = line.split('\t')
        if fields[0] == '' or len(fields) == 1:
            continue
        else:
            elements = fields[1].split(',')
            morph = {
                'surface': fields[0],
                'base': elements[6],
                'pos': elements[0],
                'pos1': elements[1],
            }
            morphs.append(morph)
    elif len(morphs):
        sentences.append(morphs)
        morphs = []

mecab_file.close()

surfaces = []
for sentence in sentences:
    cat_in = False
    for morph in sentence:
        if morph['surface'] == '猫':
            cat_in = True
            break
    if cat_in:
        for morph in sentence:
            if morph['surface'] != '猫' and morph['pos'] != '記号':
                surfaces.append(morph['surface'])

counter = collections.Counter(surfaces)
words, counts = zip(*counter.most_common(10))

plt.bar(words, counts)
plt.title('単語の出現頻度（上位10単語）')
plt.savefig('../graphs/037_words_frequency_with_cat.png')