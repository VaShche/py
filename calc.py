#my calc

str_command = input("Please type command a + b or a-b: ")

str_A = ''
str_B = ''
operation = ''
'''
-2.5 ^ -3
'''
i = 0
for letter in str_command:
	if (letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^')\
			and (operation == '') and (i > 0):
		operation = letter
	else:
		if operation == '':
			str_A = str_A + letter
		else:
			str_B = str_B + letter
	i += 1

str_A = str_A.strip()
str_B = str_B.strip()

#str_input = input("A: ")

delimoe = float(str_A)
#operation = input("+ / * - ^: ")
#str_input2 = input("B: ")

delitel = float(str_B)
result = None

if operation == '/':
	if delitel == 0:
		result = 'Inf'
	else:
		result = delimoe / delitel
elif operation == '+':
	result = delimoe + delitel
elif operation == '-':
	result = delimoe - delitel
elif operation == '*':
	result = delimoe * delitel
elif operation == '^':
	result = delimoe ** delitel
else:
	result = "unknown"

print("Result: " + str(result))
