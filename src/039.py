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
    for morph in sentence:
        if morph['pos'] != '記号':
            surfaces.append(morph['surface'])

counter = collections.Counter(surfaces)
words, counts = zip(*counter.most_common())
ranks = range(1, len(counts)+1)

plt.title('Zipfの法則')
plt.xscale('log')
plt.yscale('log')
plt.plot(ranks, counts)
plt.savefig('../graphs/039_zipf.png')