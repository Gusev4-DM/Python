import json
import decimal
import fractions
import requests

a = """
{ 
    "a": [{
            "balance": -10324.54,
            "currency": "RUB",
            "status": "NORM",
            "product_type": "Тариф"
        }, {
            "balance": 0,
            "currency": "EUR",
            "status": "CLBL",
            "product_type": "Текущий счет"
        }, {
            "balance": 0,
            "currency": "RUB",
            "status": "CLBL",
            "product_type": "Тариф"
        }, {
            "balance": 9424.64,
            "currency": "USD",
            "status": "NORM",
            "product_type": "Текущий счет"
        },{
            "balance": 2345.23,
            "currency": "RUB",
            "status": "NORM",
            "product_type": "Текущий счет"
    }]
}"""

# a_json = json.loads(a) # я специально исказил немного добавив один уровень вложенности "а" и кавычки, чтобы можно считать эту переменную модулем json.loads()

# a_new = (list(filter(lambda x: x["currency"] == "RUB", a_json["a"])))
# print(a_new)

# with open('a.json', 'w') as file:
#     json.dump(a_new, file, indent = 2)

# url = 'https://api.binance.com/api/v1/time'

# responce = requests.get(url, params={'serverTime': ''})

# price_object = responce.json()

# print(price_object)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transpose_matrix = []

# for i in range(len(matrix)):
#     transpose_row = []
#     for row in matrix:
#         transpose_row.append(row[i])
#     transpose_matrix.append(transpose_row)

# print(transpose_matrix)

# transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
# print(transpose_matrix)

    

class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_points = self.base_attack_points * level

    def attack(self, *, target: "Character") -> None:
        print(
            f'{self.character_name} attacks {target.character_name} with {self.attack_points} damage.'
            f' ({target.character_name} has {target.health_points} hp)'
        )
        
        target.health_points -= self.attack_points
        print(f'After attack {target.character_name} has {target.health_points} hp')

    def is_alive(self) -> bool:
        return self.health_points > 0

    def __str__(self) -> str:
        return f'{self.character_name} - (level: {self.level}, hp: {self.health_points}, dmg: {self.attack_points})'
    

class Ork(Character):
    base_health_points = 100
    base_attack_points = 10
    character_name = "Ork"


class Elf(Character):
    base_health_points = 50
    base_attack_points = 30
    character_name = "Elf"


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
        
    print(f'Character 1: {character_1}, is_alive {character_1.is_alive()}.')
    print(f'Character 2: {character_2}, is_alive {character_2.is_alive()}.')


ork_1 = Ork(level=2)
elf_1 = Elf(level=2)

fight(character_1=ork_1, character_2=elf_1)