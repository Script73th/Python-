print("Ввведите слово без пробелов")
str1 = input()
str2 = str1[len(str1)::-1]
if str1==str2:
    print("Yes")
else:
    print("No")