file = open('text_5.txt', 'w', encoding='utf-8')
print('Введите набор чисел,разделенных пробелами: ')
text = input()
file.write(text)
file.close()
with open('text_5.txt', 'r') as file_2:
    result = [int(i) for i in file_2.read().split()]
    print(sum(result))
