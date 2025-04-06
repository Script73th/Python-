print("Введите число")
x=int(input())
cnt=0
if x<=2000000000 and x>0:
    for i in range(1,x+1,+1):
        if x%i==0:
            cnt=cnt+1
else:
    print("Число должно быть меньше 2 миллиардов или больше 0")
print(cnt)