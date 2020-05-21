"""
Варіант 8
а) Дан текстовий файл f. Переписати у файл g всі рядки з вихідного файлу, в кінці
кожного рядка додавши знак оклику (!).
"""
file = open('f.txt', 'w')
file.write(" Lorem ipsum dolor sit amet\n consectetur adipiscing elit\n sed do eiusmod tempor incididunt ut\n labore et dolore magna aliqua")
file.close()
with open('f.txt') as f, open('g.txt', 'w') as g:
    for line in f:
        line = line.rstrip('\n')
        g.write(line + "!" + '\n')
