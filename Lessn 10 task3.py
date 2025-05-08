print("введите числа через пробле, программма будет выдавать yes или no, в зависимости наличия числа в множестве")
value = list(map(int,input().split()))
print(value)
mn=set()
counter=int(0)
for i in range(len(value)):
    counter=len(mn)
    mn.add(value[i])
    if len(mn) == counter:
        print("Yes")
    else:
        print("No")
     
print(mn)