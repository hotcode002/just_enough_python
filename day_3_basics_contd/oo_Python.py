from datetime import date

class Account : 
    def __init__ ( self, number ) :
        self.number = number
     
    def account_type(self) :
        # Get the account type
        if str(self.number).startswith("1") :
            self.type = "current"
        elif str(self.number).startswith("2") :
            self.type = "saving"
    
    def interest_rate(self) :
        
        self.account_type()
        if self.type == "current" :
            self.interest = 0
        elif self.type == "saving" :
            self.interest = 5
        return self.interest
    
    def interest_accrued(self) :
    
        # call interest_rate to determine the interest rate
        self.interest_rate()

        self.balance = 1000

        # to calculate the number of days in the year so far, include datetime above the class definition
        current_date   = date.today()
        beginning_date = date(current_date.year, 1,1)

        self.interest_accrued = self.balance * (abs(current_date - beginning_date ).days / 365) * self.interest / 100    

acc = Account(2001)
acc.interest_accrued()
print ( acc.balance )
print ( acc.interest_accrued )sd                                      5