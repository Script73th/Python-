import random
print("Эта программа создаёт 2 матрицы одинакового размера с рандомными значениями от -100 до 100. длину и ширину матрицы указывает пользователь. Программа выводит 1 матрицу, затем матрицу 2, следующая матрица 3 выводит сумму матрицы 1 и 2 ")
print("Введите ширину матрицы")
c=int(input())
print("Введите длину матрицы")
r=int(input())
matrix_1=[]
matrix_2=[]
def rt (n):
    arr=[]
    for i in range(n):
        arr.append(random.randint(-100,100))
    return arr
def sumMatrix(matr1,matr2,c,r):
    matrix_3=[]
    def summ():
        timematrix=[]
        for j in range(r):
            timematrix.append(matr1[i][j]+matr2[i][j])
        return timematrix
    for i in range(c):
        matrix_3.append(summ())
        
    return matrix_3
for i in range(r):
   matrix_1.append(rt(c)) 
for i in range(r):
   matrix_2.append(rt(c)) 
    
for i in matrix_1:
    print(*i)
print("-----------------------------------------")
for i in matrix_2:
    print(*i)
print("-----------------------------------------")
for i in sumMatrix(matrix_1,matrix_2,c,r):
    print(*i)
