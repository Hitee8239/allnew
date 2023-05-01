i = input("input first num : ")
j = input("input second num : ")

a = lambda i, j : i + j
print('{} + {} = {} '.format(i,j ,a(int(i), int(j))))