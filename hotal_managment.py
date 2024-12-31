class Managment:
    def __init__(self,balance,Acount_number):
        self.balance = balance
        self.amount = Acount_number

        print("Enter 1 for show blance:")
        print("Enter 2 for show your acount number:")
        print("Enter 3 for debit amount:")
        print("Enter 4 for credit amount:")
        print("Enter 5 for exit")
        
        user_input = input("Enter your input:")

        if user_input == "1":
            self.show_blance()
        elif user_input == "2":
            self.show_AC()
        elif user_input == "3":
            debit_amount = input("Enter your amount:")
        elif user_input == "4":
            credit_amount = input("Enter your amount:")
        elif user_input == "5":
            self.exit_from()  

    def show_blance(self):
        print(self.balance)

    def show_AC(self):

    def show_debit(self):

    def show_credit(self):
        
    def exit_from(self):





    
