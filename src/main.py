from src.classes import Operation
from src.utils import get_data


def main():
    """получаем данные из  json файла,
    переносим в новый список операции, кроме отмененных,
    сортируем по датам, затем берем 5 последних операций, и выводим на экран по заданию"""
    data = get_data()
    executed_operations = []

    for i in range(len(data) - 1):
        if data[i] == {}:
            continue

        if data[i]["state"] == "EXECUTED":
            executed_operations.append(data[i])
        else:
            continue

    for i in range(len(executed_operations) - 1):
        unsorted_operation = Operation(executed_operations[i])
        executed_operations[i]['date'] = unsorted_operation.get_date()

    executed_operations = sorted(executed_operations, key=lambda k: '.'.join(reversed(k['date'].split('.'))))

    executed_operations.reverse()
    new_operations = executed_operations[:5]

    for i in range(len(new_operations)):
        operation = Operation(new_operations[i])
        date = new_operations[i]['date']
        description = new_operations[i]["description"]
        amount = new_operations[i]["operationAmount"]["amount"]
        currency_name = new_operations[i]["operationAmount"]["currency"]["name"]

        if "from" in new_operations[i]:

            sender = operation.encode_num()[0]
            receiver = operation.encode_num()[1]

            print(f'{date} {description}\n'
                  f'{sender} -> {receiver}\n'
                  f'{amount} {currency_name}\n')
        else:

            receiver = operation.encode_num()

            print(f'{date} {description}\n'
                  f'{receiver}\n'
                  f'{amount} {currency_name}\n')


if __name__ == '__main__':
    main()
