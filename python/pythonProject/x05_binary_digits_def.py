import random

# data = random.choice(range(4, 17))
data = random .randint(4, 17)

def binary(num):
    if num//2 == 0:
        return [num%2]
    return binary(num//2) + [num%2]

print(data, "Binary number is : ",binary(data))
