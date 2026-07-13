class inventory:
    def __init__(self, Name , Price , Quantity):
        self.name = Name
        self.price = Price
        self.quantity = Quantity
    def show(self):
        print(self.name)
        print(self.price)
        print(self.quantity)

    
products = [ 
          {"Name" : "laptop" , "Price" : 85000 , "Quantity" : 10},
          {"Name"  : "Mouse" , "Price" : 1200 , "Quantity" : 25 }
]
while True:
          print("====== Inventory Management System ======")
          print("1. Show Products")
          print("2. Add Product")
          print("3. Search Product")
          print("4. Update Product")
          print("5. Sell Product")
          print("6. Delete Product")
          print("7. Save to File")
          print("8. Load from File")
          print("9. Exit")
          choice = input("Enter your choice:")
          if choice == "1":
                print("Show Products")

                for product in products:
                      print("Name:" ,  product["Name"])
                      print("Price:" , product["Price"])
                      print("Quantity:",product["Quantity"])
                      print("--------------------------")
                     
          elif choice == "2":
                print("Add Product")
                name = input("Enter Product name:")
                price = int(input("Enter Product price:"))
                quantity = int(input("Enter Product quantity:"))
                Dictionary = {
                          "Name" : name,
                          "Price" : price,
                          "Quantity" : quantity

                }
                products.append(Dictionary)
                print("Product Added Successfully")
               
            
          elif choice == "3":
                print("Search Product")
                name = input("Enter Product name:")
                found = False
                for product in products:
                      if product["Name"] == name:
                            print("product Found")
                            print("Name:" ,  product["Name"])
                            print("Price:" , product["Price"])
                            print("Quantity:",product["Quantity"])
                            print("--------------------------")
                            found = True
                            break
                if found == False:
                      print("product not found")    

          elif choice == "4":
                print("Update Product")
                name = input("Enter Product Name:")
                found = False
                for product in products:
                      if product["Name"] == name:
                            new_price = input("Enter New Price:")
                            product["Price"]= new_price
                            found = True
                            break
                if found == False:
                      print("product not found")   

                        

                           

          elif choice == "5":
                print("Sell Product")
                name = input("Enter Product Name:")
                found = False
                for product in products:
                      if product["Name"] == name:
                            quantity = int(input("Enter Product Quantity:"))
                            product["Quantity"] = product["Quantity"]-quantity
                            found = True
                            break
                if found == False:
                      print("Product not found")        
                      
          elif choice == "6":
                print("Delete Product")
                name = input("Enter Product Name:")
                found = False
                for product in products:
                      if product["Name"] == name:
                            products.remove(product)
                            found = True
                            break
                if found == False:
                      print("Product not found")     
                            
          elif choice == "7":
                print("Save to File")
                file = open("inventory.txt" , "w")
                for product in products:
                      file.write(product["Name"] + "," + str(product["Price"]) + "," + str(product["Quantity"])+ "\n")
                file.close       
                
          elif choice == "8":
                print("Load from File")
                file = open("inventory.txt", "r")
                data = file.read()
                print(data)
                file.close()

          elif choice == "9":
                print("Good Bye")
                break
               

