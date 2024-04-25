from func import full_transactions_from_date
import datetime


class Transaction:

    def __init__(self, transaction_date):
        self.transaction_date = transaction_date
        self.full_transaction_info = full_transactions_from_date(transaction_date)

    def correct_date_format(self):
        correct_date = datetime.datetime.strptime(self.transaction_date, "%Y-%m-%dT%H:%M:%S.%f")
        return correct_date.strftime('%d.%m.%Y')

