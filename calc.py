"""
Калькулятор работающий с выражениями вида 2 + 3^4 - 2.5 * -2
"""

"""Получаем команду от пользователя и очищаем её от лишних символов"""
#str_command = input("Please type command a + b or a-b: ")
str_command = input()
str_command.replace(' ', '')

"""Разделяем команду на математические операции и соответствующие им числа
Поддерживаемые мат. операции первого приоритета - возведение в степень ^
второго - деление и умножение
третьего - сложение и вычетание

Числа могут состоять из цифр от 0 до 9, точки и знака минус
"""

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = ('+', '-')
supported_ops = hp_ops + mp_ops + lp_ops
digits_chars = tuple(map(str, range(10))) + tuple('.-')

"""операции записываем в список парами: операция и число справа"""
actions = []

d = dict()
d['opr'] = 'First'
d['val'] = None
actions.append(d)

"""проходим по каждому символу в строке и разделяем на операцию или число"""
temp_str = ''
for i, letter in enumerate(str_command):
	if letter in supported_ops and (i > 0) and temp_str != '':
		actions[-1]['val'] = float(temp_str)
		temp_str = ''
		actions.append({'opr': letter,
						'val': None})
	elif letter in digits_chars:
		temp_str += letter
actions[-1]['val'] = float(temp_str)

"""вычисляем операции с высоким приоритетом"""
for i, action in enumerate(actions):
	operation = action.get('opr')
	if operation == hp_ops[0]:
		actions[i-1]['val'] = actions[i-1].get('val') ** action.get('val')
		actions.remove(action)

"""вычисляем операции со средним приоритетом"""
result = None
for i, action in enumerate(actions):
	operation = action.get('opr')
	if operation in mp_ops:
		if action.get('val') == 0 and operation == '/':
			result = 'Inf'
		else:
			actions[i-1]['val'] = eval('{0}{1}{2}'.format(actions[i-1].get('val'), operation, action.get('val')))
		actions.remove(action)

"""вычисляем операции с низким приоритетом"""
for action in actions:
	if type(result) == str:
		break

	var_A = result
	var_B = action.get('val')
	operation = action.get('opr')
	if operation in lp_ops:
		result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
	else:
		result = var_B

print("Result: " + str(result))
