import json

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

a_json = json.loads(a) # я специально исказил немного добавив один уровень вложенности "а" и кавычки, чтобы можно считать эту переменную модулем json.loads()

a_new = (list(filter(lambda x: x["currency"] == "RUB", a_json["a"])))
print(a_new)

with open('a.json', 'w') as file:
    json.dump(a_new, file, indent = 2)
