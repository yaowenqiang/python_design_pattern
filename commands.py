from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance


    def deposite(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, '
              f'balance = {self.balance}')



    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'withdraw {amount}'
                  f'balance={self.balance}')


    def __str__(self):
        return f'balance = {self.balance}'


class Command(ABC):
    def invoke(self):
        pass
    def undo(self):
        pass

class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount


    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposite(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.withdraw(self.amount)


if __name__ == '__main__':
    ba = BankAccount()
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )

    cmd.invoke()
    print(f'After $100 deposit: {ba}')



