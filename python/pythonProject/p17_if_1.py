a = int(input("Input the first number : "))
b = int(input("Input the second number : "))

# print("Max is %d" %a) if a > b else print("Max is %d" %b)

max_values = a if a > b else b

print(f'max is {max_values}')
