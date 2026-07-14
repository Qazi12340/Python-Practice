class School:
    def __init__(self  ):
        self.students = []
        self.teachers = []
        self.courses = []
    def show(self):
        print(self.students)
        print(self.teachers)
        print(self.courses)
class Student:
    def __init__(self ,name, age , marks):
        self.name = name
        self.age = age 
        self.marks = marks
    def show(self):
        print(self.name)
        print(self.age)
        print(self.marks)
class Teacher:
    def __init__(self , name , age , subject):
        self.name = name
        self.age = age
        self.subject = subject
    def show(self):
        print(self.name)
        print(self.age)
        print(self.subject)
class Course:
    def __init__(self , name , duration , teachername):
        self.name = name
        self.duration = duration
        self.teachername = teachername
    def show(self):
        print( self.name)  
        print( self.duration)  
        print( self.teachername) 
school = School()
student1 = Student("Qazi" , 18 ,95)
school.students.append(student1)
teacher1 = Teacher("Ali" ,35,"Math")
school.teachers.append(teacher1)
course1 = Course("Web Development" , 30 , "Ahmad")
school.courses.append(course1)
while True:
    print("====== School Management System ======")
    print("1. Student Management")
    print("2. Teacher Management")
    print("3. Course Management")
    print("4. Save Data")
    print("5. Load Data")
    print("6. Exit")
    choice = input("Enter Your Choice:")
    if choice == "1":
        print("============= Student Management System ==========")
        while True:
            print("1.Show Students")
            print("2.Add Student")
            print("3.Search Student")
            print("4.Update Student")
            print("5.Delete Student")
            print("6.Back")
            student_choice = input("Enter Your Choice:")
            if student_choice  == "1":
                print("Show Students")
                for student in school.students:
                    print("Name:" , student.name)
                    print("Age:" , student.age)
                    print("Marks:" , student.marks)
                    print("----------------------")
            elif student_choice == "2":
                print("Add Student")
                try:
                   student_name = input("Enter Student Name:")
                   student_age = int(input("Enter Student Age:"))
                   student_marks = int(input("Enter Student Marks:"))
                   student3 = Student(student_name , student_age , student_marks)
                   school.students.append(student3)
                   print("Student Added Successfully")
                
                except ValueError:
                         print("Invalid Input! Age aur Marks number honay chahiye.")
                                                                     
            elif student_choice == "3":
            
                print("Search Student")
                student_name = input("Enter Student Name:")
                found = False
                for student in school.students:
                    if student.name == student_name:
                        print("student found")
                        print("Name:" , student.name)
                        print("Age:" , student.age)
                        print("Marks:" , student.marks)
                        found = True
                        break
                if found == False:
                        print("student not found")
                            
            elif student_choice == "4":
              print("Update Student")
              student_name = input("Enter Student Name:")
              found = False
              for student in school.students:
                    if student.name == student_name:
                        try:
                          new_marks = int(input("Enter New Student Marks:"))
                          student.marks = new_marks
                          found = True
                          break
                        except ValueError:
                               print("Invalid Marks!")
              if found == False:
                    print("student not found")    

            elif student_choice == "5":
                print("Delete Student")
                student_name = input("Enter Student Name:")
                found = False
                for student in school.students:
                    if student.name == student_name:
                        school.students.remove(student)
                        found = True
                        break
                if found == False:
                    print("Student Not Found")
            elif student_choice == "6":
                print("Back")
                break
    elif choice == "2":
        print("======Teacher Management System======")
        while True:
            print("1.Show Teacher")
            print("2.Add Teacher")
            print("3.Search Teacher")
            print("4.Update Teacher")
            print("5.Delete Teacher")
            print("6.Back")
            teacher_choice = input("Enter Your choice:")
            if teacher_choice == "1":
               print("Show Teacher")
               for teacher in school.teachers:
                    print("Name:" , teacher.name) 
                    print("Age:" , teacher.age) 
                    print("Subject:" , teacher.subject)
                    print("---------------------------") 
            elif teacher_choice == "2":
                print("Add Teacher")
                try:
                  teacher_name = input("Enter Teacher Name:")
                  teacher_age = int(input("Enter Teacher Age:"))
                  teacher_subject = input("Enter Teacher Subject:")
                  teacher2 = Teacher(teacher_name , teacher_age , teacher_subject)
                  school.teachers.append(teacher2)
                  print("Teacher Added Successfully")
                except ValueError:
                     print("Invalid Age!")
            elif teacher_choice == "3":
              print("Search Teacher")
              teacher_name = input("Enter Teacher Name:")
              found = False
              for teacher in school.teachers:
                    if teacher.name == teacher_name:
                        print("Teacher Found")
                        print("Name:" , teacher.name) 
                        print("Age:" , teacher.age) 
                        print("Subject:" , teacher.subject)
                        found = True
                        break
              if found == False:
                print("Teacher not found")
            elif teacher_choice == "4":
              print("Update Teacher")
              teacher_name = input("Enter Teacher Name:")
              found = False
              for teacher in school.teachers:
                    if teacher.name == teacher_name:
                        try:
                          teacher_age = int(input("Enter New Age:"))
                          teacher.age = teacher_age
                          found = True
                          break
                        except ValueError:
                             print("Invalid Age!")
              if found == False:
                  print("Teacher not found")
            elif teacher_choice == "5":
              print("Delete Teacher")
              teacher_name = input("Enter Teacher Name:")
              found = False
              for teacher in school.teachers:
                    if teacher.name == teacher_name:
                        school.teachers.remove(teacher)
                        found = True
                        break
              if found == False:
                  print("Teacher not found")   
            elif teacher_choice == "6":
                print("Back")
                break

    elif choice == "3":
        print("=========Course Management========")
        while True:
            print("1. Show Courses")
            print("2. Add Course")
            print("3. Search Course")
            print("4. Update Course")
            print("5. Delete Course")
            print("6. Back")
            course_choice = input("Enter Your Choice:")
            if course_choice == "1":
                print("Show Courses")
                for course in school.courses:
                    print("Name:", course.name)
                    print("Duration:", course.duration , "Days")
                    print("Teacher Name:", course.teachername)
                    print("--------------------------------")
            elif course_choice == "2":
                print("Add Course")
                try:
                  course_name = input("Enter Course Name:")
                  course_duration = int(input("Enter Course Duration:"))
                  course_teachername = input("Enter Teacher Name:")
                  course2 = Course(course_name , course_duration , course_teachername)
                  school.courses.append(course2)
                  print("Course Added Successfully")
                except ValueError:
                      print("Invalid Duration!")
            elif course_choice == "3":
              print("Search Course")
              course_name = input("Enter Course Name:")
              found = False
              for course in school.courses:
                    if course.name == course_name:
                        print("Course Found")
                        print("Name:", course.name)
                        print("Duration:", course.duration , "Days")
                        print("Teacher Name:", course.teachername)
                        print("-----------------------------------")
                        found = True
                        break
              if found == False:
                  print("course not found") 
            elif course_choice == "4":
              print(" Update Course")
              course_name = input("Enter Course Name:")
              found = False
              for course in school.courses:
                    if course.name == course_name:
                        course_teachername = input("Enter New Teacher Name")
                        course.teachername = course_teachername
                        found = True
                        break
              if not found:
                  print("Course Not Found")   

            elif course_choice == "5":
              print("Delete Course")
              course_name = input("Enter Course Name:")
              found = False
              for course in school.courses:
                    if course.name == course_name:
                        school.courses.remove(course)
                        found = True
                        break
              if not found:
                  print("course not found")     
            elif course_choice == "6":
                print("Back")
                break
            
    elif choice == "4":
        print("Save Data")
        file = open("School.txt" , "w")
        for student in school.students:
            file.write("Student"+ ":" + student.name + "," + str(student.age)+ "," + str(student.marks)+ "\n")
        for teacher in school.teachers:
            file.write("Teacher" + ":" + teacher.name + "," + str(teacher.age)+ "," + teacher.subject + "\n")
        for course in school.courses:
            file.write("Course" + ":" + course.name + "," + str(course.duration)+ "," + course.teachername + "\n")
        file.close()    

    elif choice == "5":
        print(" Load Data")
        school.students.clear()
        school.teachers.clear()
        school.courses.clear()
        try:
           file = open("School.txt" , "r")
           for line in file:
             data = line.strip().split(":")
             info = data[1].split(",")       
             if data[0] == "Student":
                student = Student(info[0],int(info[1]) , int(info[2]))
                school.students.append(student)
             elif data[0] == "Teacher":
                teacher = Teacher(info[0], int(info[1]),info[2])
                school.teachers.append(teacher)
             elif data[0] == "Course":
                course = Course(info[0] , int(info[1]) , info[2])
                school.courses.append(course)           
           file.close()
        except FileNotFoundError:
              print("File Not Found!")
    
    elif choice == "6":
        print("Exit")
        break
          


          

            
