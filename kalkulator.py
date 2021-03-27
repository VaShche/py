"""
хотим калькулятор выражений -2 + 3.5 * 2 - 3 ^ 2
"""

#считать строчку от пользователя
instr = input('Что вычислить? ')
#instr = "-2 + 3.5 * 2 - 3 ^ 2"
print(instr)

#почистить строку 
# "-2 + 3.5 * 2 - 3 ^ 2"   ->    "-2+3.5*2-3^2"
instr = instr.replace(' ', '')



#распарсить
"""
на вход строку 
"-2+3.5*2-3^2"

на выход список словарей с операциями +-*/^ и числами

[{'opr': '', 'val': -2},{'opr': +, 'val': 3.5},{'opr': *, 'val': 2}, ...]

"""
hp_ops = tuple('^')
mp_ops = ('*', '/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple('0123456789.-')

actions = []
d = dict()
d['opr'] = 'First'
d['val'] = ''
actions.append(d)
print(actions)

# -2+3.5*2-3^-2
# [{'opr': '', 'val': '2'},{'opr': +, 'val': '3.5'},{'opr': *, 'val': 2}, ...]

for i, letter in enumerate(instr):
    if letter in supported_ops and (i > 0) and actions[-1]['val'] != '':
        """блок для операций"""
        actions.append({'opr': letter, 'val': ''})

    elif letter in digit_chars:
        """блок под числа"""
        actions[-1]['val'] += letter

print(actions)

# вычислить операции 1го приоритета (возведение в степень)
"""
на вход наш набор значение и операций
на выход обновленная ?структура данных? с операциями +- и знач

-2+3.5*2-3^2
-2+3.5*2-9
"""
i = 0
actions.reverse()
print(actions)
while i < len(actions):
    """проверить операцию в действии на соответствие операции первого приоритета
    если она не соответствуте, то ничего не делаем
    если она соответствет, то:
        - вычиляем результат для числа в этом действии и соседе СПРАВА
        - записать результат в соседа СПРАВА
        - удалить текущее действие
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in hp_ops:
        if operation == '^':
            pre_res = float(actions[i+1].get('val')) ** float(action.get('val'))
            actions[i+1]['val'] = str(pre_res)
            del actions[i]
    else:
        i += 1
actions.reverse()


#вычислить операции 2го приоритете (умножение и деление)
"""
на вход наш набор значение и операций
на выход обновленная ?структура данных? с операциями +- и знач

-2+3.5*2-9
-2+7-9
"""
i = 0
result = '0'
error = False
while i < len(actions):
    """проверить операцию в действии на соответствие операции ВТОРОГО приоритета
    если она не соответствуте, то ничего не делаем
    если она соответствет, то:
        - вычиляем результат для числа в этом действии и соседе СЛЕВА
        - записать результат в соседа СЛЕВА
        - удалить текущее действие
    """
    action = actions[i]
    operation = action.get('opr')
    if operation in mp_ops:
        if float(action.get('val')) == 0 and operation == '/':
            result = 'Inf'
            error = True
        else:
            eval_str = (actions[i-1].get('val') + operation + action.get('val'))
            pre_res = eval(eval_str)
            actions[i-1]['val'] = str(pre_res)
        actions.pop(i)
    else:
        i += 1
print(actions)
#вычислить операции 3го приоритета (сложение и вычитание)
# -2+7-9 = -4
if not error:
    for action in actions:
        var_A = result
        var_B = action.get('val')
        operation = action.get('opr')
        if operation in lp_ops:
            result = str(eval(var_A + operation + var_B))
        else:
            result = var_B
        print(result)


#вывести результат
print('Результат: {}'.format(result))