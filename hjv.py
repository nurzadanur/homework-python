class Money:
    def __init__(self, amount):
        self.__amount = amount

    def __str__(self):
        return f"<Money amount {self.amount}>"

    def __eq__(self, other):
        print(other)
        if self.amount == other.amount:
            return True
        return False


money_nora = Money(100)
money_igor = Money(200)
print(money_nora)
print(money_nora == money_igor)