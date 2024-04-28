from course_work_3.src.transaction import Transaction

t1 = Transaction("2019-08-26T10:50:58.294041")
t2 = Transaction("2019-07-03T18:35:29.512364")
t3 = Transaction("2018-03-23T10:45:06.972075")


def test_correct_date_format():
    assert t1.correct_date_format() == "26.08.2019"
    assert t2.correct_date_format() == "03.07.2019"
    assert t3.correct_date_format() == "23.03.2018"


def test_transaction_description():
    assert t1.transaction_description() == "Перевод организации"
    assert t2.transaction_description() == "Перевод организации"
    assert t3.transaction_description() == "Открытие вклада"


def test_from_account_info():
    assert t1.from_account_info() == "Maestro 1596 83** **** 5199 "
    assert t2.from_account_info() == 'MasterCard 7158 30** **** 6758 '


def test_from_account_no_info():
    assert t3.from_account_info() == 'Opening a deposit'


def test_to_account_info():
    assert t1.to_account_info() == "Счет **9589"
    assert t2.to_account_info() == "Счет **5560"
    assert t3.to_account_info() == "Счет **2431"


def test_transaction_amount_and_currency():
    assert t1.transaction_amount_and_currency() == '31957.58 руб.'
    assert t2.transaction_amount_and_currency() == '8221.37 USD'
    assert t3.transaction_amount_and_currency() == '48223.05 руб.'
