cl = []
cl2 = []
print("Введите количество чисел в 1 списке от 0 до 100000")
num1 = int(input())
print("Введите количество чисел в 2 списке от 0 до 100000")
num2 = int(input())
value = int
print("ВВедите числа через enter В 1 список чисел")
for i in range(num1):
    value=input()
    cl.append(value)
print("ВВедите числа через enter В 2 список чисел")
for i in range(num2):
    value=input()
    cl2.append(value)        
mn1 = set(cl)
mn2 = set(cl2)
print(len(mn1.intersection(mn2)))

