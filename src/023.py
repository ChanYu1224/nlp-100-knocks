import re

text_read = open('../data/england.txt')

section_lines = []
for line in text_read:
    line = line.replace('\n', '')
    if re.match(r'^={2,}.+={2,}$', line):
        section_lines.append(line)

sections = []
for line in section_lines:
    level = line.count('=')//2 - 1
    name = re.match(r'^={2,}\s*([^=\s]*)\s*={2,}$', line).group(1)
    sections.append(
        {
            'level': level,
            'name': name,
        }
    )

for section in sections:
    print('level:'+ str(section['level']) +'  name:'+ section['name'])