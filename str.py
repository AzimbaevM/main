"""строковые типы(str):
последовательность символов внутри кавычек (одинарных или двойных).
Примеры:
"""
s1 = "привет мир!"
s2 = 'Python'


# upper(): Преоброзует все символы строки в верхних регистр.

text = "Привет мир!"
upper_text = text.upper() #upper_text

#lower(): преоброзует все символы строки в нижних регистр

message = "Python"
lower_message = message.lower() #lower_message = "python"

# count(): возвращает количество вхождений подстроки в строке
sentence = 'Python - прекрасный языктпрограммирования, Python!'
count_python = sentence.count("Python") #count_python = 2

# replace(): Заменяет все вхождения одной подстроки на другую.
phrase = "Я люблю Python"
uptade_phrase = phrase.replace("Python"," программирование")

text = "Python Programming"
substring = text[0:6]
 # print(substring)


text = "salam"
print(text[::-1])


# Домашняя работа:

# strip(): Удаляет пробелы (или другие символы) с начала и конца строки
text = "   Привет, мир!   "
clean_text = text.strip()  # clean_text = "Привет, мир!"

# find(): Возвращает индекс первого вхождения подстроки (или -1, если не найдено)
text = "Python — это круто!"
position = text.find("круто")  # position = 11

# capitalize(): Делает первую букву строки заглавной, остальные — строчными
text = "python — это круто.high"
capitalized = text.capitalize()  # capitalized = "Python — это круто"

# title(): Делает заглавной первую букву каждого слова
text = "python программирование"
title = text.title()  # titled = "Python Программирование"

# rfind():  Ищет последнее вхождение подстроки и возвращает его индекс
text = "Python — мощный язык. Я люблю Python!"
last_position = text.rfind("Python")  # last_position = 27


