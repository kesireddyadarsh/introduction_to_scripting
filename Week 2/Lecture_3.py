#Welcome to Lecture_3

# trueCheck = False

# if trueCheck:
#   print("with in if block")
# else:
#     print("with in else block")
#
# print("Outside the block")


# name_1 = "Adarsh"
# roll_number_1 = 1
#
# name_2 = "Adarsh"
# roll_number_2 = 2
#
# if (name_1 == name_2) or (roll_number_1 == roll_number_2):
#     print("Both have same name with same roll number")
# else:
#     print("Both names and roll numbers may not be same")
#
# if not (name_1 == "Tom"):
#     print("Name 1 is not tom")


user_input = int(input("Enter a number"))

if user_input <= 10:
    print("User input is less than or equal to 10")
elif user_input > 10 and user_input <= 100:
    print("User input is between 10 and 100")
else:
    print("User input is greater than 100")
