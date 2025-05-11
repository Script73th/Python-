def factor (a):
    value=int(1)
    for i in range(1,a+1,+1):
        value*=i
    return int(value)
print("ВВедите целое число факториал которого будет стартовой точкой для заполнения списка")
num=int(input())
cont= factor(num)
arr=[]
for i in range(cont):
    value = factor(cont)
    arr.append(value)
    cont-=1
print (arr)
