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