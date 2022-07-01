from json import dump

with open('text_7.json', 'w', encoding='utf-8') as js_file:
    with open('text_7.txt', 'r', encoding='utf-8') as file:
        glossary = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in file}
        result = []
        for n in glossary.values():
            if n > 0:
                result.append(n)
        dump([glossary, {'Средняя прибыль: ': sum(result) / (len(result))}], js_file,
             ensure_ascii=False, indent=4)
print(result)

# честно это решение подсмотрел