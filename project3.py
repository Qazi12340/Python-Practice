class Bank:
    def __init__(self ,Name ,Account, Balance ):
        self.name = Name
        self.Account = Account
        self.Balance = Balance
    def show(self):
        print(self.name)
        print(self.account)
        print(self.Balance)
accounts = [
           {"Name" : "Qazi" , "Account" : "1001", "Balance" : 5000},
           {"Name" :   "Ali" , "Account" : "1002" , "Balance" : 10000}

]
while True:
          print("======Bank Management System=====")
          print("1. Show Accounts")
          print("2. Create Account")
          print("3. Search Account")
          print("4. Deposit Money")
          print("5. Withdraw Money")
          print("6. Delete Account")
          print("7. Save to File")
          print("8. Load from File")
          print("9. Exit")
          choice = input("Enter your choice:")
          if choice == "1":
                print("Show Accounts")
                for account in accounts:
                      print("Name:" , account["Name"] )
                      print("Account:" , account["Account"])
                      print("Balance:" , account["Balance"])
                      print("---------------")
                      
          elif choice == "2":
                print("Create Account")
                name = input("Enter your Name:")   
                account = int(input("Enter your Account:"))   
                balance = int(input("Enter your Balance:"))
                dictionary = {
                      "Name" : name,
                      "Account" : account,
                      "Balance" : balance,
                }
                accounts.append(dictionary)
                for account in accounts:
                      print("account added succefully")

          elif choice == "3":
                 print("Search Account")
                 name = input("Enter your Name:")
                 found = False
                 for account in accounts:
                     if account["Name"] == name:
                             print("Account found")
                             print("Name:" , account["Name"] )
                             print("Account:" , account["Account"])
                             print("Balance:" , account["Balance"])
                             found = True
                             break
                 if found == False:
                      print("Account not found")          
                            
          elif choice == "4":
                print("Deposit Money")
                name = input("Enter Your Name:")
                found = False
                for account in accounts:
                      if account["Name"] == name:
                            amount = int(input("Enter Deposit Balance:"))
                            account["Balance"]  = account["Balance"] + amount
                            found = True
                            break
                if found == False:
                      print("Account not found")   
                            
                            
                
          elif choice == "5":
                print("Withdraw Money")
                name = input("Enter Your Name:")
                found = False
                for account in accounts:
                      if account["Name"] == name:
                           amount = int(input("Enter Withdraw Money:"))
                           account["Balance"] = account["Balance"]- amount      
                           found = True
                           break
                if found == False:
                      print("Account not found")        

          elif choice == "6":
                print(" Delete Account")
                name = input("Enter Your Name:")
                found = False
                for account in accounts:
                      if account["Name"] == name:
                           accounts.remove(account)
                           found = True
                           break
                if found == False:
                      print("Account not found")        

          elif choice == "7":
                print("Save to File")
                file = open("bank.txt" , "w")
                for account in accounts:
                      file.write(account["Name"] + "," + str(account["Account"]) + "," + str(account["Balance"])+ "\n")
                file.close()
                      
                
          elif choice == "8":
                   print("Load from File")
                   accounts.clear()
                   file = open("bank.txt", "r")
                   for line in file:
                         data = line.strip().split(",")
                         account = {
            "Name": data[0],
            "Account": data[1],
            "Balance": int(data[2])
        }
                         accounts.append(account)
                   file.close()
        
          elif choice == "9":
                print("Good Bye")
                break

