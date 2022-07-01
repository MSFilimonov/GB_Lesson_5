my_dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open("text_4.txt", "r", encoding='utf-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_file.append(my_dictionary[i[0]] + '  ' + i[1])
with open('text_4_translate.txt', 'w+', encoding='utf-8') as file_2:
    file_2.writelines(new_file)
    file_2.seek(0)
    result = file_2.read()
    print(result)

    # Через googletrans. Хоть разобрался, как обновлять пакеты
from googletrans import Translator

with open('text_4_translateV2.txt', 'w', encoding='utf-8') as file_tr:
    with open('text_4.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        file_tr.write(Translator().translate(text, dest='ru').text)
