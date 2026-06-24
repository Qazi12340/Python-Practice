# multiplication Table
num = int(input("kaunsa table chaee :"))
for i in range(1 , 11):
    print(num , "x" , i ,"=", num * i)

#Even Number
print("\n even number:")
for i in range ( 1 , 21):
    if i % 2 == 0:
        print(i)

#sum of Numbers
total = 0
for i in range (1 , 101):
    total += i
print("\n1 se 100 tak sum", total)

#while loop - countdown
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blast off !🚀")



    
    