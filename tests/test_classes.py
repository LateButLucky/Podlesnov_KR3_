from src.classes import Operation

first_operation = Operation({
    "id": 484201274,
    "state": "EXECUTED",
    "date": "2019-04-11T23:10:21.514616",
    "operationAmount": {
        "amount": "62621.51",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Перевод с карты на карту",
    "from": "МИР 8193813157568899",
    "to": "МИР 9425591958944146"
})

second_operation = Operation({
    "id": 811920303,
    "state": "EXECUTED",
    "date": "2019-06-14T19:37:49.044089",
    "operationAmount": {
        "amount": "63150.74",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 73222753239048295679",
    "to": "Счет 78544755774551298747"
})

third_operation = Operation({
    "id": 801684332,
    "state": "EXECUTED",
    "date": "2019-11-05T12:04:13.781725",
    "operationAmount": {
        "amount": "21344.35",
        "currency": {
            "name": "руб.",
            "code": "RUB"
        }
    },
    "description": "Открытие вклада",
    "to": "Счет 77613226829885488381"
})


def test_get_date():
    assert first_operation.get_date() == "11.04.2019"


def test_encode_num():
    assert first_operation.encode_num() == ("МИР 8193 81** **** 8899", "МИР 9425 59** **** 4146")
    assert second_operation.encode_num() == ("Счет **5679", "Счет **8747")
    assert third_operation.encode_num() == ("Счет **8381")
