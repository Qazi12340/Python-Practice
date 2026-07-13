class Library:
    def __init__(self , Title , Author , Quantity):
        self.title = Title
        self.author = Author
        self.quantity = Quantity
    def show(self):
        print(self.title)
        print(self.author)
        print(self.quantity)
Books = [
        {"Title" : "Python" , "Author" : "Qazi" , "Quantity" : 5},
        {"Title" : "Java" , "Author" : "Ali" , "Quantity" : 3}
]
while True:
         print("====== Library Management System ======")
         print("1. Show Books")
         print("2. Add Book")
         print("3. Search Book")
         print("4. Update Book")
         print("5. Borrow Book")
         print("6. Return Book")
         print("7. Delete Book")
         print("8. Save to File")
         print("9. Load from File")
         print("10. Exit")
         choice = input("Enter Your Choice:")
         if choice == "1":
              print("Show Books")
              for book in Books:
                   print("Title:" , book["Title"] )
                   print("Author:" , book["Author"] )
                   print("Quantity:" , book["Quantity"] )
                   print("------------------------")
         elif choice == "2":
              print(" Add Book")
              Title = input("Enter Book Title:")
              Author = input("Enter Book Author:")
              Quantity = int(input("Enter Book Quantity:"))
              book = {
                     "Title" : Title,
                      "Author" : Author,
                      "Quantity" : Quantity
              }
              Books.append(book)
              print("Book Added Successfully")
         elif choice == "3":
              print(" Search Book")
              Title = input("Enter BOOk Title:")
              found = False
              for book in Books:
                   if book["Title"] == Title:
                        print("Book found")
                        print("Title:" , book["Title"] )
                        print("Author:" , book["Author"] )
                        print("Quantity:" , book["Quantity"] )
                        print("------------------------")
                        found = True
                        break
              if found == False:
                   print("Book not found")

         elif choice == "4":
              print("Update Book")
              Title = input("Enter Book Title:")
              found = False
              for book in Books:
                   if book["Title"] == Title:
                        Quantity = int(input("Enter New Book Quantity:")) 
                        book["Quantity"] = Quantity
                        found = True
                        break
              if found == False:
                   print("Book not found")

         elif choice == "5":
              print(" Borrow Book")
              Title = input("Enter Book Title:")
              found = False
              for book in Books:
                   if book["Title"] == Title:
                        Quantity = int(input("Enter Quantity:"))
                        if Quantity <= book["Quantity"]:
                             book["Quantity"] = book["Quantity"]-Quantity
                        else:
                             print("insufficient stock")
                        found = True
                        break
              if found == False:
                   print("Book Not Found")
            
                        
         elif choice == "6":
              print("Return Book")
              Title = input("Enter Book Title:")
              found = False
              for book in Books:
                   if book["Title"] == Title:
                        Quantity = int(input("Enter Return Quantity:"))
                        book["Quantity"] = book["Quantity"] + Quantity
                        found = True
                        break
              if found == False:
                   print("Book not Found")
         elif choice == "7":
              print("Delete Book")
              Title = input("Enter Book Title:")
              found = False
              for book in Books:
                   if book["Title"] == Title:
                        Books.remove(book)
                        found = True
                        break
              if found == False:
                   print("Book not found")
         elif choice == "8":
              print("Save to File")
              file = open("library.txt" , "w")
              for book in Books:
                   file.write(book["Title"]+ "," + book["Author"] + "," + str(book["Quantity"])+ "\n")
              file.close()    
         elif choice == "9":
              print("Load from File")
              file = open("library.txt" , "r")
              data = file.read()
              print(data)
              file.close()
         elif choice == "10":
              print("Exit")
              print("Good Bye")
              break
          