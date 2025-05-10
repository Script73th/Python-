print("Введите начало диапозона, целое число")
startvalue = int(input())
print("Введите конец диапозона, целое число")
endvalue = int(input())
arr=dict()
if startvalue< endvalue:
    for i in range (startvalue,endvalue+1):
        arr[startvalue]=startvalue**startvalue
        startvalue+=1 
elif startvalue > endvalue:
    for i in range (startvalue,endvalue-1,-1):
        arr[startvalue]=startvalue**startvalue
        startvalue-=1 
print(arr)
