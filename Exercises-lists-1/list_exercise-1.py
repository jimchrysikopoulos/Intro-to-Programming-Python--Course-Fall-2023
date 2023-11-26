#First Sub-exercise
print(" ")
numbers1=[18, 92, 75, 44, 70, 56, 40, 33, 41, 68, 49, 28]

print(numbers1)
print("=================================================")

#a
print(" ")
numbers1[1]=72

print(numbers1)
print("=================================================")

#b
print(" ")
number3 = [40]
numbers2 = []

for i in range(len(numbers1)):
    if numbers1[i] < number3[0]:
        numbers2.append(numbers1[i])

print(numbers2)

print("=================================================")

#c
print(" ")
print(sorted(numbers1))
print(sorted(numbers2))
print("=================================================")

#d
print(" ")
nb = [int(input("Give a number: "))]

j=0
while j in range(len(numbers1)):
    if numbers1[j] == nb[0]:
        print("Your number's position in the list is: " + str(numbers1.index(int(nb[0])) + 1))
    else:
        print("Your number is not in this list")
    break

print("=================================================")


#Second Sub-exercise
print(" ")
usernames=[]

print(" Menu: ")
print("1. Register User")
print("2. Delete account")
print("0. EXIT")

print(" ")


counter = 1
ans =input("|Choose one of the three options (0, 1, 2): ")
               

while counter == 1:

    while ans == '1':

        if usernames == []:
            print(" ")
            usn = (input("Your username is: "))
            usernames.append(usn)
            print("Your username has been saved successfuly")
            print("List" + str(usernames))
            print(" ")
            ans_1 = input("|Choose one of the three options (0, 1, 2): ")
            ans = str(int(ans_1))

        elif usernames != []:
            usn = (input("Your username is: "))
            usn_1 = [usn]

            for t in range(len(usernames)):
                if usernames[t] == usn_1[0]:
                    print("Your username is already saved")
                    print("List" + str(usernames))
                    print(" ")
                    break

            for k in range(len(usernames)):
                if usernames[t] != usn_1[0]:
                    usernames.append(usn)
                    print("Your username has been saved successfuly")
                    print("List" + str(usernames))
                    print(" ")
                    break
                
            ans_2 = input("|Choose one of the three options (0, 1, 2): ")
            ans = str(int(ans_2))
            print(" ")

    while ans == '2':

        if usernames == []:
            print("You do not have any usernames")
            print(" ")
            ans_3 = input("|Choose one of the three options (0, 1, 2): ")
            ans = str(int(ans_3))

        elif usernames != []:
            usn = (input("The username you want to delete is: "))
            usn_3 = [usn]

            for t in range(len(usernames)):
                if usernames[t] == usn_3[0]:
                    usernames.remove(usn)
                    print("Your username has been deleted successfuly")
                    print("List" + str(usernames))
                    print(" ")
                    break
            for k in range(len(usernames)):
                if usernames[t - 1] != usn_3[0]:
                    print("Your username is not in the list")
                    print("List" + str(usernames))
                    print(" ")
                    break

            ans_4 = input("|Choose one of the three options (0, 1, 2): ")
            ans = str(int(ans_4))
            print(" ")

    while ans == '0':
        print("See you again soon!")
        counter = 0
        break

print("=================================================")


#Third Sub-exercise
print(" ")
import random

add_number = 100
list = []

for i in range(add_number):
    list.append(random.randint(1, 1000))

print("List: " + str(list))

print(" ")
print("The maximum amount is: " + str(max(list)))
print("The minimum amount is: " + str(min(list)))
total = sum(list)
print("The total amount is: " + str(total))
print("The average amount is: " + str(total/add_number))

print("=================================================")


#Forth Sub-exercise
print(" ")
print(sorted(list))

for j in range(len(list)):
    if list[j] == list[j - 1]:
        print(" ")
        print ("The duplicate number is: " + str(list[j]))

print(" ")
