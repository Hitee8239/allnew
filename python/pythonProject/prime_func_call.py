import prime_func

a = int(input("input number : "))
b = prime_func.prime(a)

if(b):
    print("not prime number")
else:
    print("prime number")