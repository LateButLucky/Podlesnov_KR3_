from src.utils import splitting_text_numbers, encode_count_num
import datetime


class Operation:
    def __init__(self, operation_data):
        self.operation_data = operation_data

    def encode_num(self):
        """
        Метод, использующий функцию которая возвращает скрытый счет/номер
        :return: возвращает кортеж счета или карты
        """
        if "from" in self.operation_data:
            sender = splitting_text_numbers(self.operation_data["from"])
            receiver = splitting_text_numbers(self.operation_data["to"])
            sender[1] = encode_count_num(sender[1])
            receiver[1] = encode_count_num(receiver[1])
            sender_new = " ".join(sender)
            receiver_new = " ".join(receiver)
            return sender_new, receiver_new

        else:
            receiver = splitting_text_numbers(self.operation_data["to"])
            receiver[1] = encode_count_num(receiver[1])
            receiver_new = " ".join(receiver)
            return receiver_new

    def get_date(self):
        """
        Метод возвращающий переделанный формат даты
        """
        operation_time = self.operation_data['date']
        change_time = operation_time.split('T')
        operation_time_new = " ".join(change_time)
        date_time_obj = datetime.datetime.strptime(operation_time_new, '%Y-%m-%d %H:%M:%S.%f')
        new_time = date_time_obj.strftime('%d.%m.%Y')
        return new_time
