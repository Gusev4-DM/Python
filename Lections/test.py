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

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix = []

for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)

print(transpose_matrix)

transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix)