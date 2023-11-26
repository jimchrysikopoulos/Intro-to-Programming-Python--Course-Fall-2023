#Third Sub-exercise
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

print("===============================================================================================")