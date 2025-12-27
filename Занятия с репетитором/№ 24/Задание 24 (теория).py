''''''
'''
1. Через позиции ненужного / нужного элемента. Проходимся по строке и записываем все индексы в лист pos.
2. Регулярки. Через finditer(pattern, text) и через re.search(pattern, text) с использованием сдвига.
3. Двойные указатели
4. Указатели через методы модуля re (re.finditer(pattern, text); match.start(); match.end(); re.search(pattern, text))
'''

# := моржовый опертор (эквивалентен match = re.search(pattern, text), а после while match:)
'''
https://education.yandex.ru/ege/task/7cecbe1f-be24-497e-8c28-cab3dc437d2f

Текстовый файл состоит из символов A, B и C.

Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.

Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.

Для выполнения этого задания следует написать программу.

# Доступен файл для чтения: 24.txt
import re

pattern = r"(AB|CB)+"

with open("24.txt") as file:
  text = file.readline()

max_len = 0
for match in re.finditer(pattern, text):
  max_len = max(max_len, len(match.group())) # match.group() - text[match.start():match.end()]

print(max_len//2)
'''



