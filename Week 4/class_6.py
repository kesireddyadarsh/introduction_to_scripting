# """
# Author:Adarsh
# MOdifed: Test
# Date:
# """



#this is to print
def function_1():
    print("function 1")

#this is to print
def function_2():
    print("fucntion 2")

class test_class():
    def __init__(self,number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def addition(self):
        print("Addition result",self.number_1 + self.number_2)

    def printing(self):
        print("Test class")

if __name__ == '__main__':
    obj_1 = test_class(5,10)
    obj_1.printing()
    obj_1.addition()

    obj_2 = test_class(100,20)
    obj_2.addition()

    object_list = []
    object_list.append(obj_1)
    object_list.append(obj_2)

    object_list[0].addition()
