def printList (list,x):
    if len(list)==x:
        print("конец списка")
        return
    print(x)
    printList(list,x+1)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
value=my_list[0]
printList(my_list, value)