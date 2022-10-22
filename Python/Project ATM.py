## Creat ATM Class
class Atm:
    # initialization => constructor
    def __init__ (self, acc_no, name, passwd, balance):
        self.acc_no = acc_no
        self.name = name
        self.passwd = passwd
        self.balance = balance

    def __str__(self):
        return "Automatic Teller Machine"

    # ATM Method 1 Account Summary
    def acc_sum(self):
        print(f"Account No.     : {self.acc_no}")
        print(f"Account Name    : {self.name}")
        print(f"Account Balance : {round(self.balance,2)}")

    # ATM Method 2 Deposite
    def deposit(self, d_amount):
        self.balance += d_amount
        print(f"Account No. {self.acc_no} {self.name}")
        print(f"Balance = {self.balance}")

    # ATM Method 3 Withdraw
    def withd(self, w_amount):
        self.balance -= w_amount
        print(f"Account No. {self.acc_no} {self.name}")
        print(f"Balacee = {self.balance}")

    # ATM Method 4 Change Password
    def chg_pass(self):
        print("Change Password")
        count = 1
        while count < 4:
            old_pass = input("Enter the old password:")
            if self.passwd == old_pass:
               self.passwd = input("Enter the new password:")
               print(f"your passwaord already changed to: {self.passwd}")
               break
            else:
               count = count + 1
               print(f"You enter wrong password! Pleas Try again #{count}")

atm1 = Atm(1234567890120, "Mr. Attapol Aiem", "123456", 100000)
atm2 = Atm(1234567890121, "Mrs. Jarivun Aiem", "222222", 200000000)

atm2.acc_sum()
atm1.acc_sum()
