#simple div
str_input = input("A: ")

delimoe = float(str_input)
#print(type(delimoe))

operation = input("+ / * - ^: ")

str_input2 = input("B: ")

delitel = float(str_input2)
#print(type(delitel))
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
#print(type(result))

print("Result: " + str(result))