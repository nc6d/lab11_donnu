"""
Варіант 8
б) Дано текстові файли f і g. Записати в файл h спочатку компоненти файлу f, потім
- компоненти файлу g зі збереженням порядку.
"""
f = open('f.txt', 'w')
g = open('g.txt', 'w')
h = open('h.txt', 'w')
f.write("\tLorem ipsum dolor sit amet\n consectetur adipiscing elit\n"
        " sed do eiusmod tempor incididunt ut\n "
        "labore et dolore magna aliqua\n")
g.write('\tExcepteur sint occaecat\n cupidatat non proident\n'
        ' sunt in culpa qui officia deserunt mollit\n'
        ' anim id est laborum.')
f.close()
g.close()
with open('f.txt') as f, open('g.txt') as g:
    for line in f:
        h.write(line)
    for line in g:
        h.write(line)
