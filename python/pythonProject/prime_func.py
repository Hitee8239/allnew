

def prime(a):
    flag = False
    if a == 1:
        print("not prime number")
    elif a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                flag = True
            break
        if flag:
            return True
        else:
            return False

