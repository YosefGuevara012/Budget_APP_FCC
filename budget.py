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
        self.ledger.append({"amount": -1 * amount , "description": description})
        self.budget -= amount
        return True
      else:
        return False

    def get_balance(self):
        return self.budget

    def check_funds(self, amount):
        if self.budget >= amount:
          # print("TRUE")
          return True
        else:
          # print("FALSE")
          return False


    def __str__(self):

        title = self.name.center(30, "*") + "\n"
        transactions = ""
        for transaction in self.ledger:
      
          if len(transaction['description']) < 23:
              transactions += str(transaction['description']) + spaces(transaction) + str(transaction['amount']) + "\n"
          else:
              transactions += str(transaction['description'])[0:23] + (7 - len(str(transaction['amount']))) * " " + str(transaction['amount']) + "\n"
          
        total = "Total: " + str(self.budget)
        message = title + transactions + total 

        
        return message
        

      
        

        
        
      
      





def create_spend_chart(categories):
    pass

def spaces(transaction):

  return (30 - len(str(transaction['description']) + str(transaction['amount']))) * " "