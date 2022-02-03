"""
Contains lecture 3
This is demonstration of list
"""
names = ["Adarsh","Ram","Sam",1,2,3]
print(names)
print(names[0])
names.append(["Tam"])
print(names)
print(names.pop())

"""
This is for while
"""
# This is find odd and even program
#Assingment bouns question
loop_counter = 1
while loop_counter <= 10:
    print(loop_counter)
    if loop_counter%2 == 0:
        print(loop_counter)
    loop_counter += 1 #Here we are increasing loop count by 1


# This is to find factorial number
factNumber = 5
loop_counter_1 = 1
result_fact_number = 1
while loop_counter_1 <= factNumber:
    result_fact_number = result_fact_number *loop_counter_1
    # print(loop_counter_1)
    loop_counter_1 += 1
print(result_fact_number)

# This is to remove empty elements in a given string of list
lst_names = ["Adarsh","Ram","Sam","Tam","","Jam","","Ham"]
new_list = []
loop_counter_2 = 0
while loop_counter_2 < len(lst_names):
    print(lst_names[loop_counter_2])
    if(lst_names[loop_counter_2] != ""):
        new_list.append(lst_names[loop_counter_2])
    loop_counter_2 += 1
print(new_list)

"""
This is for loop
"""
#This is to declare the for loops
values = [1,2,3,4]

lst_names = ["Adarsh","Ram","Sam","Tam","","Jam","","Ham"]
for tempVariable in values:
    print(tempVariable)

for tempVariable in range(0,len(lst_names)):
    print(lst_names[tempVariable])

#This is to find the exponential of list to its index
new_list = []
for num in range(0, len(values)):
    print("This is just num", num)
    print("This is the number from loop  ",values[num])
    # print("Expo:  ",values[num]**values[num])
    new_list.append(values[num]**values[num])
    # print("List:: ",new_list)
print(new_list)

# This is for nested for loop
numbers = [1,2,3]
questions =["what","when","why"]
for v_1 in numbers:
    print(v_1)
    for v_2 in questions:
        print(v_2)

#This is for printing mulitplication table 
for temp_1 in range(1,11):
    for temp_2 in range(1,11):
        print(temp_1* temp_2, end =' ')
    print()
