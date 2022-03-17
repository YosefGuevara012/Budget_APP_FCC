class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.budget = 0
        self.withdraws = 0

    def deposit(self, amount, description = ""):
        self.amount = amount
        self.ledger.append({"amount": self.amount, "description": description})
        self.budget += amount

    def withdraw(self, amount, description = ""):
      if self.check_funds(amount) == True:
        self.ledger.append({"amount": -1 * amount , "description": description})
        self.budget -= amount
        self.withdraws += amount
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


    def transfer(self, amount, category):
        self.withdraw(amount, "Transfer to " + str(category.name))
        category.deposit(amount, "Transfer from " + str(self.name))
        
  
    def __str__(self):

        title = self.name.center(30, "*") + "\n"
        transactions = ""
        for transaction in self.ledger:
      
          if len(transaction['description']) < 23:
              spaces = (30 - len(str(transaction['description']) + str(transaction['amount']))) * " "
              transactions += str(transaction['description']) + spaces + str(transaction['amount']) + "\n"
          else:
              transactions += str(transaction['description'])[0:23] + (7 - len(str(transaction['amount']))) * " " + str(transaction['amount']) + "\n"
          
        total = "Total: " + str(self.budget)   
        balance = title + transactions + total 

        return balance

      
def create_spend_chart(categories):
  
    percentages = ["100| ", " 90| ", " 80| ", " 70| ", " 60| ", 
                   " 50| ", " 40| ", " 30| ", " 20| ", " 10| ", 
                   "  0| "]

    expenses = ""
    total_expenses = 0
  
    for category in categories:
      total_expenses += category.withdraws
      

    pct_category = []

    for category in categories:
      pct_category.append(round(category.withdraws/total_expenses * 100, 0))
      
    print(pct_category)
  
    title = "Percentage spent by category\n"

    for percentage in percentages:
      
      expenses += percentage 
      

    return title + expenses

    
