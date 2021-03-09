#my calc

str_command = input("Please type command a + b or a-b: ")
str_command.replace(' ', '')

str_A = ''
str_B = ''
operation = ''
'''
-2.5^-3
'''

for i, letter in enumerate(str_command):
	if letter in '+-*/^' and (operation == '') and (i > 0):
		operation = letter
	else:
		if operation == '':
			str_A = str_A + letter
		else:
			str_B = str_B + letter

var_A = float(str_A)
var_B = float(str_B)
result = None

if operation in '+-*/':
	if var_B == 0 and operation == '/':
		result = 'Inf'
	else:
		result = eval('{0}{1}{2}'.format(var_A, operation, var_B))
elif operation == '^':
	result = var_A ** var_B
else:
	result = "unknown"

print("Result: " + str(result))
