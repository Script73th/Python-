n=int(input("ВВедите количество чисел"))
arr=[]
for i in range(n):
    a=int(input())
    if a>=1 and a<=10000:
        arr.append(a)
    else:
        print("Введите число от 1 до 10000")
arr.reverse()
print(arr)