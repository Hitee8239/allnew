coffee = 5
price = 20000
print("우리 매장 커피는{} 잔 있습니다 ".format(coffee))

money = int(input("돈을 넣어주세용 : "))

print("{}원을 넣었음 ".format(money))

amount = int(input("커피 몇잔 살거임 ? :"))
print("{}잔 샀음 ".format(amount))

change = money - price
print("거스름돈은 {}원이며 , 커피 {}잔을 판매합니다.".format(change, amount))

print("남은 커피양은  {}입니다".format(coffee-amount))