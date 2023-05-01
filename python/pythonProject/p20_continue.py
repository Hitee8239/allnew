# while True:
sums = 0
for i in range(1,10):
    if i % 2 == 0 :
        continue
    sums += i
    print(f'sum += {i}')
print()
print(f"sum = {sums}")


