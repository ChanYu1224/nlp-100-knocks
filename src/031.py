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

for sentence in sentences:
    for morph in sentence:
        if morph['pos'] == '動詞':
            print(morph['surface'])
