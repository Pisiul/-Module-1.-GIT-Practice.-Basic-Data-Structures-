
#************************************************ Домашнее задание *****************************************************
#***************************************** ( Строки и Индексация строк ) ***********************************************


#                             Практическое задание по уроку "Строки и индексация строк"
#
#
# Цель: Научиться работать со строками и индексацией строк в Python.
#
# Задаие №1:
#
# Выполните следующие действия в PyCharm:
#    В переменную example запишите любую строку.
#    Выведите на экран(в консоль) первый символ этой строки.
#    Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
#    Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
#    Выведите на экран(в консоль) это слово наоборот.
#    Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
#
# Примечания:
#    Для вывода значений на экран используйте функцию print()
#    Для доступа к символу строки по индексу используйте квадратные скобки и индекс символа ('Urban'[3]
#    -  четвёртый символ строки 'Urban' - 'a') Индексация начинается с нуля.

#-----------------------------------------------------------------------------------------------------------------------

# Ответ:
# Задание №1:

example = "Hello my name is Denis and iam student at Urban Academy"
print(example[1]) # - e/
print(example[-1]) # - y/
print(example[54]) # - y/  не забываем пробелы тоже символы.
print(example[:22]) # - Hello my name is Denis
print(example[-32:]) # - and iam student at Urban Academy
print(example[::-1]) # - ymedacA nabrU ta tneduts mai dna sineD si eman ym olleH
print(example[0:54:2]) # - Hlom aei ei n a tdn tUbnAae

#-----------------------------------------------------------------------------------------------------------------------
#D:\Программы\ProjectPyton\BasiesStructures\Scripts\python.exe "D:\Программы\ProjectPyton\Module 1.
# GIT Practice. Basic Data Structures\Strings and String Indexing (Homework).py"
# e
# y
# y
# Hello my name is Denis
# and iam student at Urban Academy
# ymedacA nabrU ta tneduts mai dna sineD si eman ym olleH
# Hlom aei ei n a tdn tUbnAae

# Process finished with exit code 0
#-----------------------------------------------------------------------------------------------------------------------


























