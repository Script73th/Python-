print("Введите сколько будет чисел")
n=int(input())
cnt=0
for i in range(n):
    print("Введите число")
    value=int(input())
    if(value==0):
        cnt=cnt+1
print(cnt)


