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
    for i in range(len(sentence)):
        articulation = ''
        offset = 0
        while (i+offset) < len(sentence) and sentence[i+offset]['pos'] == '名詞':
            articulation += sentence[i+offset]['surface']
            offset += 1
        if offset > 1:
            i += offset-1
            print(articulation)
