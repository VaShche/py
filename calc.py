# my calc

str_command = input("Please type command a + b or a-b: ")
# str_command = input()
str_command.replace(' ', '')

'''
parsing
'''

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = ('+', '-')
supported_ops = hp_ops + mp_ops + lp_ops
digits_chars = tuple(map(str, range(10))) + tuple('.,-')

str_A = ''
str_B = ''
actions = []

d = dict()
d['opr'] = 'None'
d['val'] = ''
actions.append(d)

for i, letter in enumerate(str_command):
	if letter in supported_ops and (i > 0) and actions[-1].get('val') != '':
		actions.append({'opr': letter,
						'val': ''})
	elif letter in digits_chars:
		actions[-1]['val'] = actions[-1].get('val') + letter

'''
calculation
'''
#variables = list(map(float, variables))
for action in actions:
	action['val'] = float(action.get('val'))

result = actions[0].get('val')

for action in actions:
	if type(result) == str:
		break
	print(action)
	var_A = result
	var_B = action.get('val')
	operation = action.get('opr')

	if operation in '+-*/':
		if var_B == 0 and operation == '/':
			result = 'Inf'
		else:
			result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
	elif operation == '^':
		result = var_A ** var_B
	else:
		result = var_A

print("Result: " + str(result))
