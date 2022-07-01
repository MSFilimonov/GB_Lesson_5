file = open('poem.txt', 'r', encoding='utf-8')
lines = file.readlines()
print(lines)
file.seek(0)
for i in range(len(lines)):
    line = file.readline()
    words = line.split()
    print(f'Строка номер: {i + 1} количество слов: {len(words)}')
