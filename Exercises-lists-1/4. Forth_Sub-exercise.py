#Forth Sub-exercise
print(" ")
print(sorted(list))

for j in range(len(list)):
    if list[j] == list[j - 1]:
        print(" ")
        print ("The duplicate number is: " + str(list[j]))

print(" ")