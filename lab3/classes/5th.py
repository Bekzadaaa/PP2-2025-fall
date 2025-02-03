class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Вы внесли {amount}. Новый баланс: {self.balance}")
        else:
            print("Сумма депозита должна быть больше 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Вы сняли {amount}. Новый баланс: {self.balance}")
            else:
                print("Недостаточно средств для снятия.")
        else:
            print("Сумма снятия должна быть больше 0.")

owner = input("Введите имя владельца счета: ")
initial_balance = float(input("Введите начальный баланс счета: "))

account = BankAccount(owner, initial_balance)

while True:
    action = input("Вы хотите внести или снять деньги? (введите для депозита '1' или для снятия '2', или '3' для выхода): ").lower()
    
    if action == '1':
        amount = float(input("Введите сумму для депозита: "))
        account.deposit(amount)
    elif action == '2':
        amount = float(input("Введите сумму для снятия: "))
        account.withdraw(amount)
    elif action == '3':
        print("Завершаю программу.")
        break
    else:
        print("Неверная команда. Пожалуйста, введите 'депозит', 'снятие' или 'выход'.")
