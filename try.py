import collections
pets = dict()

def pets_list(id):
    print("Список питомцев")
    print("---------------")
    for pet in pets:
        print(f'Имя: {pets[id]['имя']}, Вид: {pets[id]["вид"]}, Возраст: {suffix(pets[id]["возраст"])}')

def create():
    print('Введите информацию о питомце')
    name = input('Введите имя питомца: ')
    species = input('Введите вид питомца: ')
    age = int(input('Введите возраст питомца: '))
    owner_name = input('Введите владельца питомца: ')
    if pets:
        last_id = collections.deque(pets.keys(), maxlen=1)[0]
        new_id = last_id + 1
    else:
        new_id = 1
        pets[new_id] = {'имя': name, 'вид': species, 'возраст': age, 'владелец': owner_name}

def suffix(age):
    if 11 <= age % 100 <= 14:
        return f"{age} лет"
    elif age % 10 == 1:
        return f"{age} год"
    elif age % 10 in [2, 3, 4]:
        return f"{age} года"
    else:
        return f"{age} лет"

def delete(pet_id):
    if pet_id in pets:
        del pets[pet_id]
        print(f"Питомец с идентификатором {pet_id} удален.")
    else:
        print("Питомец с таким идентификатором не найден.")

def update(pet_id, name=None, species=None, age=None):
    pet = pets.get(pet_id) if pet:
    if name:
        pet['name'] = name
    if species:
        pet['species'] = species
    if age is not None:
        pet['age'] = age
        print(f"Информация о питомце с ID {pet_id} обновлена.")
    else:
        print(f"Питомец с ID {pet_id} не найден.")

def pets_id(pet_id):
    if pet_id in pets:
        print(pets[pet_id])
    else:
        print(False)

while True:
    command = input("Введите команду (или 'stop' для выхода) : ")
    if command.lower() == 'stop':
        print("Команда 'stop' получена. Завершение программы.")
    break