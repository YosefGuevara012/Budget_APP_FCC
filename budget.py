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
        category.deposit(amount, "Transfer from " + str(self.name))
        return self.withdraw(amount, "Transfer to " + str(category.name))
        
  
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
  

  
    total_expenses = 0
    strings = []
  
    for category in categories:
        total_expenses += category.withdraws
        strings.append(category.name)
      
    pct_category = []

    for category in categories:
        pct_category.append(round(category.withdraws/total_expenses * 100, 0))
      

    rounded = []
    for pct in pct_category:
        if pct % 10 > 5:
            rounded.append((pct // 10 + 1) * 10 )
        else:
            rounded.append((pct // 10) * 10 )

      
    # print(rounded)
  
    title = "Percentage spent by category\n"

    percentages = ["100| ", " 90| ", " 80| ", " 70| ", " 60| ", 
                   " 50| ", " 40| ", " 30| ", " 20| ", " 10| ", 
                   "  0| "]


    expenses = ""
    counter = 110
    for percentage in percentages:
      
        counter = counter - 10
        expenses += percentage 

        for value in rounded:
          if counter > value:
            expenses += "   "
          else:
            expenses += "o  "
            
        expenses += "\n" 

    line = (" "* 4) + "-" + ("---"* len(rounded)) + "\n"

  
    longest = 0
    for text in strings:
      if len(text) > longest:
        longest = len(text)
        

    for i in range(len(strings)):
      strings[i] = strings[i] + " " * (longest - len(strings[i]))

    
    bottom = ""

    for i in range(len(strings[0])):
      bottom += "    "
      for text in strings:
        bottom += " " + text[i] + " "

      bottom += "\n"


    return title + expenses + line + bottom

    
