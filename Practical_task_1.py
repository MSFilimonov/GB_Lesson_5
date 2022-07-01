file = open('prog_file.txt', 'w', encoding='utf-8')
print('Введите текст: ')
while True:
    text = input()
    file.write(text + '\n')
    if text == '':
        break
file.close()
