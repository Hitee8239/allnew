while True:
    n = input("input number : (q : quit) : ")

    if n == 'q':
        break
    elif n == range(1,10):
        print("input number range 2~9")
        continue
    else:
        for i in range(1,10):
            print(f'{n}* {i} = {int(n)*i}')




