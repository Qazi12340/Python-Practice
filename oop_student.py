class student:
        def __init__(self, name , marks):
               self.name = name
               self.marks = marks
        def result(self):
         if self.marks >= 50:
             print(f" {self.name}_ pass! marks:{self.marks}")
         else:
            print(f"{self.name}_ fail! marks:{self.marks}")
s1 = student( "Ali", 75)
s2 = student("Ahmad", 40)
s3 = student("sara", 90)
s1.result()
s2.result()
s3.result()
        