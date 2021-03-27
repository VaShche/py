import os

students = ['Щемелинин Вадим Леонидович']
with open('students.txt', 'r') as f:
    students += f.readlines()

symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
           u"abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA")

tr = {ord(a): ord(b) for a, b in zip(*symbols)}

intro = '''"""
{}
редактируйте/пишите код в блоках между
---начало--- и ---конец---
Решение задачи может быть в несколько строчек, но чем меньше, тем лучше.
В случае верного решения запуск файла приведёт к выводу True для каждого задания
"""
'''

def task(descr, var_name, var_value):
    task_txt = '''
""" Задание №{0}
{1}
---------------начало блока редактирования----------------"""

{2}

"""------------ конец блока редактирования----------------"""
print('№{0} ' + str({2} == {3}))
'''
    global task_id
    task_id += 1
    return task_txt.format(task_id, descr, var_name, var_value)


for s in students:
    s = s.strip()
    task_id = 0
    fio4filename = s.translate(tr).split(' ')
    with open(os.path.join('tasks1', '{0}{1}_self_check1.py'.format(fio4filename[0], fio4filename[1][0])), 'w') as f:
        f.write(intro.format(s))

        f.write("a = '{}'".format(s))

        res = s.split(' ')
        f.write(task("Запишите в переменную 'fio' список, полученный из переменной 'а' и содержащий Фамилию, Имя, Отчество",
                     'fio', res))
        res = res[1]
        f.write(task("Получите только имя из переменной 'fio' и запишите в переменную 'name'",
                     'name', "'{}'".format(res)))
        res = len(s.split(' ')[0])
        f.write(task("Получите в переменной 'l' длину своей фамилии",
                     'l', res))
        res = s.split(' ')[0][2]
        f.write(task("Получите в переменной 'res' строку из третей буквы вашей Фамилии",
                     'res', "'{}'".format(res)))
        res = s.split(' ')[0][:2]
        f.write(task("Получите в переменной 'res' строку из двух первых букв вашей Фамилии",
                     'res', "'{}'".format(res)))
        res = s.split(' ')[0][-2:]
        f.write(task("Получите в переменной 'res' строку из двух последних букв вашей Фамилии",
                     'res', "'{}'".format(res)))
        res = list(s.split(' ')[0])
        f.write(task("Получите в переменной 'surname_list' список из букв вашей Фамилии по очереди",
                     'surname_list', res))
        res = tuple(s.split(' ')[0])
        f.write(task("Получите в переменной 'surname_tuple' кортеж из букв вашей Фамилии по очереди",
                     'surname_tuple', res))
        l = len(s.split(' ')[0])
        res = list(range(2, l, 2))
        f.write(task("Получите в переменной 'res' список чётных чисел от 1 до длины вышей фамилии",
                     'res', res))
        res = list(enumerate(s.split(' ')[0]))
        f.write(task("Получите в переменной 'res' список кортежей где первый элемент кортежа это номер буквы в вашей фамилии (от 0), а второй это буква вашей фамилии",
                     'res', res))
        res = list(s.split(' ')[0])
        res.reverse()
        f.write(task("Получите в переменной 'res' из переменной surname_list список букв вашей фамилии наоборот",
                     'res', res))
        res = list(s.split(' ')[0])
        res.reverse()
        res = ''.join(res)
        f.write(task("Получите в переменной 'res' из переменной fio строку с вашей фамилией задом наперёд",
                     'res', "'{}'".format(res)))
        res = list(s.split(' ')[0])
        res.remove(res[2])
        f.write(task("Получите в переменной 'res' из переменной surname_list список букв вашей фамилии без третей буквы",
                     'res', res))







