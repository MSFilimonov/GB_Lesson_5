with open('text_3.txt', 'r', encoding='utf-8') as file:
    cont = file.readlines()
    file.seek(0)
    salary = []
    for i in range(len(cont)):
        line = file.readline()
        my_list = line.split()
        if float(my_list[1]) < 20000:
            print(my_list[0])
        salary.append(my_list[1])
    print(f'Средняя величина дохода сотрудников: {sum(map(float, salary)) / len(salary)}')
