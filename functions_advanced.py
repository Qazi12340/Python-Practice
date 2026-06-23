#basic Function

def subtract(a , b):
    return a - b
print(subtract(10,4))

#default parameter

def greet(name , city = "Lahore"):
    return("Hello" " "+ name +" " "from"" " + city)
print(greet("Tuheed"))
print(greet("Tuheed" , "Karachi"))

# lambda 

is_even = lambda x : x % 2 == 0
print(is_even(4))

#map

nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x : x ** 2 , nums))
print(squared)