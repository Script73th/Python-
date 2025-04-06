print ("Введите первое число")
a=int(input())
print ("Введите первое число")
b=int(input())
if(a<=b):
    for i in range(a,b+1,):
        if i%2==0:
            print(i,end=" ")
        
else:
    print("Неверный диапозон чисел")