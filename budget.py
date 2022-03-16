class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0

    def deposit(self, amount, description = ""):
        self.amount = amount
        self.ledger.append({"amount": self.amount, "description": description})
        self.budget += amount

    def withdraw(self, amount, description = ""):
      if self.check_funds(amount) == True:
        self.ledger.append(amount * -1)
        self.budget -= amount
        return True
      else:
        return False

    def get_balance(self):
        return self.budget

    def check_funds(self, amount):
        if self.budget >= amount:
          print("TRUE")
          return True
        else:
          print("FALSE")
          return False
        
        

      
        

        
        
      
      





def create_spend_chart(categories):
    pass