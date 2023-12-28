from src.utils import get_data, splitting_text_numbers, encode_count_num


def test_get_data():
    assert type(get_data()) == list
    assert type(get_data()[1]) == dict


def test_encode_count_num():
    assert encode_count_num('9425591958944146') == '9425 59** **** 4146'
    assert encode_count_num('78544755774551298747') == '**8747'


def test_splitting_text_numbers():
    assert splitting_text_numbers('МИР 9425591958944146') == ['МИР', '9425591958944146']
    assert splitting_text_numbers("Счет 78544755774551298747") == ['Счет', '78544755774551298747']

