# Урок 1. Базовые операции

# Вывод данных в консоль
# print(<данные>) - выводит данные в консоль
# print(<данные 1>, <данные 2>...) - множественный вывод данных в консоль

# Форматы вывода данных
# print(<данные 1>, <данные 2>..., sep=<строка>) - вывод данных в консоль, с разделителем между ними в виде строки
# print(<данные 1>, <данные 2>..., sep=<строка 1>, end=<строка 2>) - end ставит в конце вывода всех данных строку 2

# Специальные символы в строке
# \n - перенос на новую строку
# \t - создание табуляции
# \ - указание того, что идущий впереди символ не является частью программы

# Математические действия
# + - сложение
# - - вычитание
# * - умножение
# / - деление
# ** - возведение в степень
# // - деления нацело
# % - остаток от деления

# Математические функции
# min(<последовательность чисел>) - возвращает минимальное число из последовательности
# max(<последовательность чисел>) - возвращает максимальное число из последовательности
# abs(<число>) - возвращает модуль числа
# pow(<число>, <степень>) - возвращает число в/во <степень> степени
# round(<число>) - возвращает ближайшее целое число к <число>

# Получение данных от пользователя
# input(<данные>) - выводит <данные>, а потом запрашивает у пользователя данные и возвращает их


# Урок 2. Переменные и типы данных
# Переменная - это именованная ячейка в памяти компьютера, позволяющая сохранить данные и получить к ним доступ

# Создание переменной
# <название> = <значение> - создание переменной
# <название 1>, <название 2> = <значение 1>, <значение 2> - создание множества переменных

# Работа с переменной
# Переменную можно выводить, производить с ней операции, переназначать и т.д.
# del <переменная> - удаляет переменную из памяти компьютера, тем самым её очищая
# В переменных можно хранить различные данные, сейчас об этом как раз и будет речь

# Типы данных
# int - целое число
# float - число с точкой
# str - строка
# bool - логическое выражение - True / False - истина / ложь

# Явное приведение типов данных
# <тип данных>(<значение>) - возвращает значение в указанном типе данных
# стоит уточнить, что 0, преобразованный в bool, равняется False, а все остальные числа равняются True

# Неявное приведение типов данных
# Неявное приведение типов данных происходит при помощи самой программы, а не нас

# Сокращённые математические операции
# <переменная> <операция>= <значение> - эквивалентно записи <переменная> = <переменная> <операция> <значение>


# Урок 3. Условия
# Условие - это выражение логического типа, которое принимает либо True (истина), либо False (ложь)

# Простое условие
# if <условие>:
#     <блок кода> - если условие равняется True, то выполняется блок кода
# Условия можно вкладывать друг в друга

# Типы условий
# == - равно
# != - не равно
# < - меньше
# > - больше
# <= - меньше или равно
# >= - больше или равно

# Сокращённые условия
# if <переменная> (True) / not <переменная> (False):]
#     <блок кода> - сокращённая проверка переменных с типом данных bool на их значение

# Оператор "elif"
# elif <условие 2>:
#     <блок кода 2> - дополнительное условие, срабатывает когда главное условие оказалось неверным

# Оператор "else"
# else:
#     <блок кода> - срабатывает в том случае, когда все условия оказались неверными

# Логические операторы
# and - логическое И
# or - логическое ИЛИ
# not - логическое НЕ

# Тернарный оператор
# <значение 1> if <условие> else <значение 2> - возвращает значение в зависимости от того, верное условие или нет


# Урок 4. Циклы
# Цикл - это управляющая конструкция, которая заставляет какой-то блок кода выполняться несколько раз

# Цикл "for"
# for <название> in range(<старт>, <стоп>, <шаг>):
#     <блок кода> - создаёт переменную с названием <название> и значением <старт>, и пока данная переменная меньше, чем
# <стоп>, прибавляет к этой переменной <шаг> и выполняет блок кода. Переменную можно свободно вызывать внутри тела цикла

# Перебор строки
# for <название> in <строка>:
#     <блок кода> - полностью перебирает указанную строку, в качестве значения для переменной идут символы строки

# Цикл "while"
# while <условие>:
#     <блок кода> - пока условие верное, будет выполняться блок кода

# Бесконечный цикл
# while True: ... - бесконечный цикл

# Циклические операторы
# break - полностью завершает выполнение цикла
# continue - переходит на следующую итерацию цикла

# Конструкция for / else
# for i in <строка>:
#     <тело цикла>
# else:
#     <блок кода> - выполняет блок кода только тогда, когда цикл полностью прошёлся по строке


# Урок 5. Списки
# Список - это набор данных, каждое из которых имеет свой индекс, позволяющий быстро получить к нему доступ
# Тип данных - list

# Создание списка
# <название> = [<данные>*] - создаёт список с названием <название> и помещает внутрь него данные

# Работа с элементами списка
# <название списка>[<индекс элемента>] - обращение к элементу списка
# Важно помнить, что индексы всегда начинаются с 0, а не с 1!
# С элементами списка можно всяко взаимодействовать, так же как и с переменными

# Функции для работы со списком
# count(<элемент>) - возвращает количество элементов в списке
# index(<элемент>, <порядковый номер>) - возвращает индекс элемента в списке по порядковому номеру
# sort() - сортирует список в порядке возрастания
# reverse() - переворачивает список
# copy() - возвращает полную копию списка
# append(<элемент>) - добавляет элемент в конец списка
# extend([<элементы>*]) - добавляет несколько элементов в конец списка
# insert(<индекс>, <элемент>) - заменяет элемент по <индекс> индексу на <элемент>
# pop(<индекс>) - удаляет элемент по <индекс> индексу
# remove(<элемент>, <порядковый номер>) - удаляет элемент из списка по порядковому номеру в списке
# clear() - полностью очищает список

# Заметки
# Перебор строки так же работает и для списка, только вместо символа там элемент списка


# Урок 6. Функции для работы со строками и срезы
# Строка - это список, где в качестве элементов списка выступают символы строки

# Функции для работы со строками
# upper() - возвращает строку в верхнем регистре
# lower() - возвращает строку в нижнем регистре
# capitalize() - возвращает строку в виде "Aa"
# isupper() - возвращает, находится строка в верхнем регистре или нет (True / False)
# islower() - идентично, но только с нижним регистром
# len() - возвращает длину строки, работает так же и для списков
# count(<символ>) - возвращает количество символа в строке
# find(<символ>, <порядковый номер>) - возвращает индекс символа в строке по порядковому номеру
# split(<разделитель>) - разделяет строку по разделителю и преобразовывает в список
# isalpha() - возвращает, состоит ли строка полностью из букв (True / False)
# isnumeric() - идентично, но только с цифрами

# Срезы
# Сразу стоит упомянуть, что срезы работают так же и для списков
# <строка>[<старт>, <стоп>, <шаг>] - возвращает отрезок строки от символа с индексом <старт> (включительно)
# до символа с индексом <стоп>, переходя при этом каждый раз на <шаг> символ вперёд
# Для списков срезы работают идентично, но вместо символов элементы списка


# Урок 7. Кортежи
# Кортеж - это список, в котором все элементы являются константами (неизменяемыми)
# Тип данных - tuple

# Создание кортежа
# <название> = (<элементы>*) - создание кортежа с названием <название>

# Функции для работы с кортежами
# count() и index()

# Важные заметки
# Для создания кортежа необязательно указывать круглые скобки
# Если в скобках нет последовательности, то это не кортеж!
# Например, (5,) является кортежем, а (5) уже нет


# Урок 8. Словари
# Словарь - это неупорядоченная структура данных, позволяющая хранить пары "ключ-значение"
# Тип данных - dict

# Создание словаря
# <название> = {<ключ>: <значение>**} - создание словаря, где для каждого значения есть свой ключ, по которому
# его можно вызвать в программе

# Альтернативная запись словаря
# <название> = dict(<ключ>=<значение>**)

# Обращение к элементам словаря
# for <ключ>, <значение> in <словарь>.items():
#     <блок кода> - вызывает функцию items(), которая возвращает объект с ключами и значениями словаря и сохраняет
# их в переменные <ключ> и <значение>, которые можно свободно вызывать в блоке кода

# Функции для работы со словарями
# get(<ключ>) - возвращает значение ключа
# keys() - возвращает все ключи словаря в виде списка
# values() - идентично, но возвращает значения
# popitem() - удаляет последний элемент словаря
# В состав функций также входят уже известные функции clear(), pop(<ключ>) и copy()
