from course_work_3.src.transaction import Transaction

t1 = Transaction("2019-08-26T10:50:58.294041")
t2 = Transaction("2019-07-03T18:35:29.512364")
t3 = Transaction("2018-03-23T10:45:06.972075")


def test_correct_date_format():
    assert t1.date_format_correction() == "26.08.2019"
    assert t2.date_format_correction() == "03.07.2019"
    assert t3.date_format_correction() == "23.03.2018"


def test_transaction_description():
    assert t1.get_transaction_description() == "Перевод организации"
    assert t2.get_transaction_description() == "Перевод организации"
    assert t3.get_transaction_description() == "Открытие вклада"


def test_from_account_info():
    assert t1.get_from_account_info() == "Maestro 1596 83** **** 5199 "
    assert t2.get_from_account_info() == 'MasterCard 7158 30** **** 6758 '


def test_from_account_no_info():
    assert t3.get_from_account_info() == 'Opening a deposit'


def test_to_account_info():
    assert t1.get_to_account_info() == "Счет **9589"
    assert t2.get_to_account_info() == "Счет **5560"
    assert t3.get_to_account_info() == "Счет **2431"


def test_transaction_amount_and_currency():
    assert t1.get_transaction_amount_and_currency() == '31957.58 руб.'
    assert t2.get_transaction_amount_and_currency() == '8221.37 USD'
    assert t3.get_transaction_amount_and_currency() == '48223.05 руб.'
