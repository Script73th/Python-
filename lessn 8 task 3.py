print("Введите максимальную грузоподъемность лодки")
m = int (input())
if(m>=1) and (m<=1000000):
    print("ВВедите количество рыбаков от 1 до 100")
    n = int (input())
    warray=[]
    if(n>=1) and (n<=100):
       
        print("Введите массу каждого рыбака через enter")
        for i in range(n):
            a = int (input())
            warray.append(a)
            if(a>m):
                print("Вес одного из рыбаков выше чем грузоподъемность лодки")
                quit()
        count=0
        vallueEnd=0
        warraysize = len(warray)       
        for j in range(warraysize):
            index= 0 
            for k in range(1,len(warray)):
               vallue = int(warray[0]+warray[k])
               if(vallue<=200):
                   
                   if vallue >vallueEnd:
                       vallueEnd = vallue
                       index = k

            if len(warray) > 1:
                warray.pop(index)
                warray.pop(0) 
                warraysize=warraysize - 2
                count = count +1
                if warraysize == 0:
                    print("Требуемое количество лодок - ", count) 
                    quit()
                elif warraysize == 1:
                    count = count+1
                    print("Требуемое количество лодок - ", count) 
                    quit()
            
            vallueEnd=0   
    else:
        print(" не корректное число рыбаков")
else:
    print("Число не того диапозона")