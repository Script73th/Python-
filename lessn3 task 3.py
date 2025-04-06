print ("Введите минимальную сумму инвестиций ")
mincash = int (input())
print ("Введите количесвто денег Ivan")
ivancash = int (input())
print ("Введите количесвто денег Mike")
mikecash = int (input())

if(ivancash>=mincash) and (mikecash>=mincash):
    print("2")
elif (ivancash>=mincash) and (mikecash<mincash):
    print("Ivan")
elif (ivancash<mincash) and (mikecash>=mincash):
    print("Mike")   
elif (ivancash<mincash) and (mikecash<mincash):
    if ivancash + mikecash >= mincash:
        print("1")
    else:
        print("0")   