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