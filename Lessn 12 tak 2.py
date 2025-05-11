import collections
pets = dict()
def get_suffix(age):
    newAge=""
    if (age>4 and age<21) or (age>104 and age<121):
        newAge= str(age) + ' лет'
    elif age ==1 or age%10==1:
        newAge= str(age) + ' год'
    elif (age>1 and age<5)or(age%10==2)or(age%10==3)or(age%10==4):
        newAge= str(age) + ' года'
    elif (age>101 and age<105):
        newAge= str(age) + ' года'
    else:
        newAge= str(age) + ' лет'
    return newAge
def create():
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
        name ["Возраст"] = get_suffix(age)
        print("Введите имя хозяина")
        humanName = input()
        name["Имя хозяина"]= humanName
        if pets:
            last = collections.deque(pets, maxlen=1)[0]
            new_id = 1 + last
            pets[new_id] = name
            print ("Ваш персональный номер животного: ",new_id) 
        else:
            new_id = 1
            pets[new_id] = name
            print ("Ваш персональный номер животного: ",new_id) 
def read ():
    print("Введите персональный номер вашего питомца")
    findID = int (input())
    if get_pet(findID):
        print(pets.get(findID))
def pets_list ():
    print("Список питомцев клиники")
    print("-----------------------")
    for i in pets:
        print (i,". ",pets.get(i))
def update ():
    print("Введите персональный номер животного ")
    petID = int(input())
    if  get_pet(petID):
        print("Введите новые данные")
        print("Введите имя вашего питомца") 
        updateName = input()
        updateAnimalName = updateName
        updateName = dict()
        updateName['Имя:'] = updateAnimalName
        print("Введите тип вашего питомца")
        updateAnimal = input()
        updateName ['Тип питомца'] = updateAnimal 
        print("Введите возраст вашего питомца")
        updateAge=int(input())
        updateName ["Возраст"] = get_suffix(updateAge)
        print("Введите имя хозяина")
        updateHumanName = input()
        updateName["Имя хозяина"]= updateHumanName
        pets[petID] = updateName   
def delete():
    print("Введите персонльный номер животного чтобы удалить карточку")
    petID = int(input())
    if  get_pet(petID):
        pets.pop(petID)
        print("Карточка успешно удалена!")
def get_pet(ID):
    if ID in pets.keys():
        return pets[ID]
    else:
        return print("Такого номера карточки животного в базе данных нет")
x=0
command =""
print("Здравствуйте. Добро пожаловать в Ветклинику.")
while command != 'stop':
    print("Для Добавления карточки питомца введите  create")
    print("Для просмотра карточки                   read")
    print("Для изменения карточки питомца введите   update")
    print("Для удаления карточки питомца введите    delete")
    print("Для выхода из программы введите          stop")
    print("Вывести весь список животных клиники     all")
    command = input()
    if command == "create" or command == "Create":
        create()
    elif command == "read" or command == "Read":
        read()
    elif command == "update" or command == "Update": 
        update()
    elif command == "delete" or command == "Delete":
        delete()
    elif command == "all" or command == "All":
        pets_list()