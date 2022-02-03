#This is lecture 5
# def printing():
#     print("Todays class")
#
# printing()
# printing()

#Multiple calls for functions
# def function_1():
#     num_1 = 10
#     num_2 = 10
#     print("Addition ", num_1+num_2)
#     function_2()
#
# def function_2():
#     num_1 = 10
#     num_2 = 10
#     print("Subtraction ", num_1-num_2)
#
# function_1()


# def calculator():
#     number_1 = int(input("Enter first number"))
#     number_2 = int(input("Enter Second number"))
#     operation = int(input(" 0 addition 1 subtraction 2 multiple"))
#     if operation == 0:
#         addition(number_1, number_2)
#     elif operation == 1:
#         subtraction(number_1, number_2)
#     elif operation == 2:
#         mulitplication(number_1, number_2)
#
# def addition(number_1, number_2):
#     print("Addition of inputs ", number_1+number_2)
#
# def subtraction(number_1, number_2):
#     print("subtraction of inputs ", number_1-number_2)
#
# def mulitplication(number_1, number_2):
#     print("multiple of inputs ", number_1*number_2)
#
# def main():
#     for temp in range(0,10):
#         calculator()

#return
# def return_function():
#     num1 = 10
#     num2 = 4
#     num3 = num1**num2
#     return num3
#
# def main():
#     returned_value = return_function()
#     print("retrun value is ",returned_value)
#
# main()


# def calculator():
#     number_1 = int(input("Enter first number"))
#     number_2 = int(input("Enter Second number"))
#     operation = int(input(" 0 addition 1 subtraction 2 multiple"))
#     output = 0
#     if operation == 0:
#         output = addition(number_1, number_2)
#     elif operation == 1:
#         output = subtraction(number_1, number_2)
#     elif operation == 2:
#         output = mulitplication(number_1, number_2)
#     print("This is out_put ", output)
#
# def addition(number_1, number_2):
#     return number_1+number_2
#
# def subtraction(number_1, number_2):
#     return number_1-number_2
#
# def mulitplication(number_1, number_2):
#     return number_1*number_2
#
# def main():
#     calculator()
#
# main()

# def main():
#     lst_names = ["tam","jam","","sam","","ham"]
#     print(remove_empty_names(lst_names))
#
# def remove_empty_names(lst_names):
#     new_list = []
#     for temp in lst_names:
#         if temp != "":
#             new_list.append(temp)
#     return new_list
#
# main()

# variable_1 = 10
# def temp_2():
#     variable_2 = 20
#     global variable_3
#     variable_3 = 30
#
# def main():
#     temp_2()
#     print("variable_1 ", variable_1)
#     print("variable_2 ", variable_2)
#     print("variable_3 ", variable_3)
#
# main()

# import random

# new_list = []
# for temp in range(0,10):
#     number = random.randint(1,100)
#     print(number)
#     new_list.append(number)
#
# print(new_list)

# new_list = [random.randint(1,100) for i in range(0,10)]
# print(new_list)
