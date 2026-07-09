class Contact:
    def __init__(self, name , phone  ):
          self.name = name
          self.phone = phone
    def show(self):
          print(self.name)
          print(self.phone)

contacts = [
      
           {"name"  : "Ali" , "phone" : 3444784348},
           {"name" : "Qazi" , "phone" : 3427656347}
      
  ]
        
while True:
          print("===== Contact Book =====")
          print("1. Show Contacts")
          print("2. Add Contact")
          print("3. Search Contact")
          print("4. Update Contact")
          print("5. Delete Contact")
          print("6. Save to File")
          print("7. Load from File")
          print("8. Exit")
          choice = input("Enter your choice:")
          if choice == "1":
                print("Show contact")
               
                for contact in contacts:
                    print("Name :" , contact["name"])
                    print("Phone:" ,contact["phone"])
                    print("-----------------------")
          elif choice == "2":
                print("Add Contact ")
                name = input("Enter Your Name:")
                phone = input("Enter Phone")
                dictionary = {
                       "name" : name,
                        "phone" : phone
                }
                contacts.append(dictionary)
                for contact in contacts:
                       print("Contact Added Successfully.")
                      
                
          elif choice == "3":
                print("Search Contact ")
                name = input("Enter your name :")
                found = False
                for contact in contacts:
                      if contact["name"]== name:
                            print("contact found")
                            print("Name:", contact["name"])
                            print("Phone :", contact["phone"])
                            found = True
                            break
                if found == False:
                   print("contact not found")

          elif choice == "4":
                print("Update Contact ")
                name = input("Enter Your Name:")
                found = False
                for contact in contacts:                    
                    if contact["name"] == name:
                      new_phone  = input("Enter your New Phone Number:")
                      contact["phone"] = new_phone
                      found = True
                      break
                if found == False:
                      print("contact not found")
                  
          elif choice == "5":
                print("Delete Contact ")
                name = input("Enter Your Name:")
                found = False
                for contact in contacts:
                     if contact["name"] == name:
                          contacts.remove(contact)
                          found = True
                          break
                if found == False:
                     print("contact not found")
                          
          elif choice == "6":
                print(" Save to File")
                file = open("contact.txt","w")
                for contact in contacts:
                     file.write( contact["name"] + "," + str(contact["phone"])+ "\n")
                file.close()
          elif choice == "7":
                print(" Load from File ")
                file = open("contact.txt" , "r")
                data = file.read()
                print(data)
                file.close

          elif choice == "8":
              print("Good Bye")
              break 
         

          