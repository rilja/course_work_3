from func import full_transactions_from_date
import datetime


class Transaction:

    def __init__(self, transaction_date):
        self.transaction_date = transaction_date
        self.full_transaction_info = full_transactions_from_date(transaction_date)

    def correct_date_format(self):
        correct_date = datetime.datetime.strptime(self.transaction_date, "%Y-%m-%dT%H:%M:%S.%f")
        return correct_date.strftime('%d.%m.%Y')

    def transaction_description(self):
        transaction_description = self.full_transaction_info.get("description")
        return transaction_description

    def from_account_info(self):
        from_account_info = self.full_transaction_info.get("from")
        if from_account_info is None:
            return f''
        txt_in_info = from_account_info.split()
        card_name = []
        for txt in txt_in_info:
            if txt.isdigit():
                card_number = txt
            else:
                card_name.append(txt)
        secret_card_number = list(card_number)
        for num in range(6, 12):
            secret_card_number[num] = "*"
        for num in range(4, 16, 5):
            secret_card_number.insert(num, " ")
        secret_card_number = ''.join(secret_card_number)
        full_card_name = ' '.join(card_name)
        new_from_account_info = full_card_name + " " + secret_card_number

        return new_from_account_info


