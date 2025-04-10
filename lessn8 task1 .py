n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    if a>=1 and a<=10000:
        arr[i]=a
    else:
        print("Введите число от 1 до 10000")
arr.reverse()
print(arr)