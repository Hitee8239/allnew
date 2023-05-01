import calc_func

a = int(input("input first number : "))
b = int(input("input Second number : "))

print('{} + {} ={}'.format(a,b,calc_func.add(a,b)))
print('{} - {} ={}'.format(a,b,calc_func.sub(a,b)))

print('{} % {} ={}'.format(a,b,calc_func.div(a,b)))
print('{} / {} ={}'.format(a,b,calc_func.divmo(a,b)))