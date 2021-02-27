#simple div
str_input = input()

varA = int(str_input)

str_input2 = input()

varB = int(str_input2)

operation = input()

if operation == '/':
    result = varA / varB
else:
    result = "???"

print(result)
