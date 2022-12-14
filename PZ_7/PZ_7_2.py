# 2. Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
# строке, заменив в нем все предыдущие вхождения его последней буквы на символ
# «.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ».
# Количество пробелов между словами не изменять.
import re

income_words = re.findall(r'\w*', input("Введите строку: "))
pattern = (lambda word: word[:-1].replace(word[-1], ".") + word[-1] if word else " ")
answer = "".join(list(map(pattern, income_words)))
print(f"Ответ - {answer}")
