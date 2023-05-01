def min(a,b):
    if a > b :
        return b
    else:
        return a

a= input("Input First number :  ")
b= input("Input First number :  ")

print("{} vs {} : Min number = {}".format(a,b,min(a,b)))