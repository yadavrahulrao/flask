class BankAccount:
  def __init__(self,acc_no ,name,date_of_open , balance ):
    self.acc_no = acc_no
    self.date_of_open = date_of_open
    self.balance = balance
    self.name = name

  def deposite(self,amount):
    self.balance += amount
    return("Deposited:",amount,"Balance:",self.balance)

  def debit(self,amount):
    if amount <= self.balance :
      self.balance -= amount
      return("Debited:",amount,"Balnce:",self.balance)
    else :
      return("not sufficient balance")

  def CheckBalance(self):
    return("Balance:",self.balance)

account = BankAccount(1001003067,"Rahul","01-03-2004",9000)

# account.CheckBalance()

# account.deposite(25000)

# account.debit(4000)

# account.CheckBalance()