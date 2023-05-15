import x04_factorial_def
class Factorial(object):
    def __init__(self , data):
        self.data = data
    def factorial(self):
        n = 1
        for i in range(1 , self.data + 1):
            n =  n* i
        return n
input = int(input("input num : "))
fact = Factorial(input)
print(f'{input} factorail = {fact.factorial()}')

Factorial.factorial()