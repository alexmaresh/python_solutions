# Задача 1. Выведите все элементы, которые меньше 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
res = [x for x in a if x < 5]

# Задача 2. Вернуть список, который состоит из элементов, общих для этих двух списков.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
res = [x for x in a if x in b]

# Задача 3. Отсортируйте словарь по значению в порядке возрастания и убывания.
d = {'4': '660', '1': '123', '2': '234', '3': '567'}
d_u = sorted(d.items(), key=lambda item: item[1], reverse=True)
d_v = sorted(d.items(), key=lambda item: item[1])
sorted_v = {k: v for k, v in d_v}
sorted_u = {k: v for k, v in d_u}

# Задача 4. Напишите программу для слияния нескольких словарей в один.
b = {'key': 'value', 'foo': 'bar'}
d = {'4': '660', '1': '123', '2': '234', '3': '567'}
res = {**d, **b}

# Задача 5. Найдите три ключа с самыми высокими значениями в словаре
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
result = sorted(my_dict, key=my_dict.get, reverse=True)[:3]

# Задача 6.Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
print(int('ABC', 16))


# Задача 7. Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы, а каждое число внутри равно сумме двух расположенных над ним чисел.
def pascal_triangle(n):
    row = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

# Задача 8. Проверка на палиндром.

def palindrom(x: str):
    x = x.lower()
    return x == x[::-1]

# Задача 9. Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')

#Задача 10. Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами
# usernums = map(int,input().split(','))
# l = list(usernums)
# t= tuple(l)

#Задача 11. Выведите первый и последний элемент списка.
lst_t = [1,2,3,9]
print(lst_t[0], lst_t[-1])

#Задача 12. Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

def extension(filename):
    filename_parts = filename.split('.')
    if len(filename_parts) < 2:  # filename has no dots
        raise ValueError('the file has no extension')
    first, *middle, last = filename_parts
    if not last or not first and not middle:
        # example filenames: .filename, filename., file.name.
        raise ValueError('the file has no extension')
    return filename_parts[-1]

# Задача 13
# При заданном целом числе n посчитайте n + nn + nnn.
def three_sums(n):
    n2 = int(str(n)*2)
    n3 = int(str(n) * 3)
    return n + n2 + n3

# Задача 14. Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

def stop_if(n:list):
    for i in n:
        if i == 237:
            break
        if i % 2==0:
            print(i)

# Задача 15. Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
a = [1,2,3,4]
b = [1,2,3]
x = [x for x in a if x not in b]
print(x)

#Ну или через множества
set_1 = set(['White', 'Black', 'Red'])
set_2 = set(['Red', 'Green'])
print(set_1 - set_2)

#Задача 17. Сложите цифры целого числа
def sum_digits(n):
    sum = 0
    for i in str(n):
        sum+=int(i)
    return sum

# Задача 18. Посчитайте, сколько раз символ встречается в строке.
s = 'Foobar'
print(s.count('o'))

# Задача 19. Поменяйте значения переменных местами.
a = 1
b = 2
a,b = b,a

#Задача 20. С помощью анонимной функции извлеките из списка числа, делимые на 15.
nums = [30,6,234,678]
result = list(filter(lambda x: not x % 15, nums))

#Задача 21.Нужно проверить, все ли числа в последовательности уникальны.
def all_unique(numbers):
    return len(numbers) == len(set(numbers))

# Задача 22. Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
import collections

text = 'lorem ipsum dolor sit amet amet amet'

words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

