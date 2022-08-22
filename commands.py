from abc import ABC
from enum import Enum

class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance


    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, '
              f'balance = {self.balance}')



    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'withdraw {amount}, '
                  f'balance = {self.balance}')
            return True
        return False


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
        self.success = None


    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)



if __name__ == '__main__':
    ba = BankAccount()
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )

    cmd.invoke()
    print(f'After $100 deposit: {ba}')
    cmd.undo()
    print(f'After $100 deposit undone: {ba}')


    illegal_cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITHDRAW, 1000
    )

    illegal_cmd.invoke()
    print(f'After impossible withdrawal: {ba}')
    illegal_cmd.undo()
    print(f'After undone: {ba}')




