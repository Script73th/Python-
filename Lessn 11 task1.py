animalID = 0
pets= dict()
x=0
while x<1:
    print("Здравствуйте. Добро пожаловать в Ветклинику. Для Добавления карточки питомца введите add, для просмотра карточки Open")
    command = input()
    if command == "add":
        print("Введите имя вашего питомца") 
        name = input()
        animalName = name
        name = dict()
        name['Имя:'] = animalName
        print("Введите тип вашего питомца")
        animal = input()
        name ['Тип питомца'] = animal 
        print("Введите возраст вашего питомца")
        age=int(input())
        newAge=""
        if age>4 and age<21:
            newAge= str(age) + ' лет'
        elif age ==1 or age%10==1:
            newAge= str(age) + ' год'
        elif (age>1 and age<5)or(age%10==2)or(age%10==3)or(age%10==4):
            newAge= str(age) + ' года'
        name ["Возраст"] = newAge
        print("Введите имя хозяина") 
        humanName = input()
        name["Имя хозяина"]= humanName
        animalID = animalID +1
        pets[animalID] = name
        print ("Ваш персональный номер животного: ",animalID) 
    elif command == "open":
        print("Введите персональный номер вашего питомца")
        findID = int (input())
        print(pets.get(findID)) 
     

