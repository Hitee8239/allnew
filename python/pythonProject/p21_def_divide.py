def divide(a,b):
    return (a/b ,a%b)


a= int(input("Input First number :  "))
b= int(input("Input second number :  "))
print('{}/{}'.format(a,b))
print("Quotient {}".format(int(divide(a,b)[0])))
print("Remainder {}".format(divide(a,b)[1]))