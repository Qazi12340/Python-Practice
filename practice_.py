class Student:
    def __init__(self , name ,age ,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)
    def update_marks(self, marks):
        self.marks = marks
    def check_result(self , ):
        if self.marks >= 50:
             print("pass")
        else:
            print("fail")
student1 = Student("Ali", 18 ,95)
student2 = Student("Qazi",19,96)
students = [student1 , student2]


while True:
          

    print("===== Student Management System =====")
    print("1. Show Student")
    print("2. Search Student")
    print("3. Add Student")
    print("4. Delete Student")
    print("5. Update Marks")
    print("6. Save File")
    print("7. Load File")
    print("8. Exit")

    choice = input("Enter Choice: ")

     
    if choice == "1":
        print("Show Student")

        for student in students:
            student.show()
    elif choice == "2":
        print("Search Student")
        name = input("Enter Your Name: ")
        found = False
        for student in students:
            if student.name == name:
                 student.show()
                 found = True
        if found == False:
           print("student not found")


    elif choice == "3":
        print("Add Student")
        name1 = input("enter your name:")
        age1 = int(input("enter your age:"))
        marks1 = int(input("enter your marks:"))
        student3 = Student(name1 , age1 , marks1)
        students.append(student3)
        for student in students:
         student.show()

    elif choice == "4":
        print("Delete Student")
        name = input("Enter Your Name:" )
        for student in students:
             if student.name == name:
                 students.remove(student)
                 break
        for student in students:
             student.show()
                     
                 


    elif choice == "5":
        print("Update Marks")
        name = input("Enter Student Name: ")
        found = False
        for student in students:
             if student.name == name:
                 marks = int(input("Enter New Marks: "))
                 student.update_marks(marks) 
                 found = True 
        if found == False:
             print("Student not found")
    elif choice == "6":
        print("Save File")
        file = open("student.txt", "w")
        for student in students:
            file.write(  student.name + "," + str(student.age) + "," + str(student.marks)+ "\n")
        file.close()
        print("File Saved Successfully")            

    elif choice == "7":
        print("Load File")
        file = open("student.txt" ,"r")
        data = file.read()
        print(data)
        file.close()
    
    elif choice == "8":
        break
       
    
    
    
    




   
 
        
class Student:
    def __init__(self , name ,age ,marks):
        self.name = name
        self.age = age
        self.marks = marks
    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)
    def update_marks(self, marks):
        self.marks = marks
    def check_result(self , ):
        if self.marks >= 50:
            print("pass")
        else:
            print("fail")
        

       
student1 = Student("Ali", 18 ,95)
student2 = Student("Qazi",19,96)
student1.update_marks(99)
 
student1.check_result()
students = [student1 , student2]
name = input("Enter Your Name :")
found = False
for student in students:
    
    if student.name == name:
        student.show()
        found = True
    
if found == False:
    print("student not found")
name1 = input("enter your name:")
age1 = int(input("enter your age:"))
marks1 = int(input("enter your marks:"))
student3 = Student(name1 , age1 , marks1)
students.append(student3)
for student in students:
    student.show()
name = input("Enter Your Name:" )
for student in students:
    if student.name == name:
        students.remove(student)
for student in students:
    student.show()
    
file = open("student.txt", "w")

for student in students:
    file.write(  student.name + "," + str(student.age) + "," + str(student.marks)+ "\n")
file.close()
file = open("student.txt" ,"r")
data = file.read()
print(data)
file.close()

      
    
    