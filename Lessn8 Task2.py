count = int(input("Введите кол чисел в массиве, каждое число должно быть от 1 до 100000"))
if(count>=1) and (count<=10000):
    print("Введите числа в массив через пробел")
    array=list(map(int,input().split()))
    if len(array)==count :
        array.append(array[0])
        array.pop(0)
        print(array)
    else:
        print("количество чисел введенных в массив не равно переданному числу")          
else:
    print("Не корректное число")