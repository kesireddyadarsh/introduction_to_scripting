# print("This is test")

# def main():
#     outfile = open('Testfile.txt','w')
#     outfile.write('This is first line \n')
#     outfile.write('This is second line \n')
#     outfile.write('This is third line \n')
#     outfile.write('This is fourth line \n')
#     outfile.close()
#
# main()


# def main():
#     append_object = open('Testfile.txt','a')
#     append_object.write('This is test \n')
#     append_object.close()
#
#     infile = open('Testfile.txt','r')
#     file_contents = infile.read()
#     infile.close()
#     print(file_contents)
#
# main()

# def main():
#     infile = open('Testfile.txt','a')
#     infile.write('This is fifth line \n')
#     infile.write('This is sixth line \n')
#     infile.close()
#
# main()

# def main():
#
#     try:
#         infile = open('Testfile_1.txt','r')
#         file_contents_1 = infile.readline()
#         file_contents_2 = infile.readline()
#         infile.close()
#         print(file_contents_1)
#         print(file_contents_2)
#     except :
#         print('In Exception')
#
#
#
#     number_4 = 10
#     number_5 = 10
#     number_sum = number_4+ number_5
#     print(number_sum)
#
#
# main()

# def main():
#     numb_obj = open('numbers.txt','r')
#     number = 0
#     for line in numb_obj:
#         number += line
#     print(number)
#     numb_obj.close()
#
# main()


# def main():
#     number_1 = int(input('Enter a number'))
#     number_2 = int(input('Enter a number'))
#     if number_2 != 0:
#         number_3 = number_1/number_2
#         print(number_3)
#     else:
#         print('Enter a good nuimber')
#
#     number_4 = 10
#     number_5 = 10
#     number_sum = number_4+ number_5
#     print(number_sum)
#
# main()









# def main():
#     num_1 = 0
#     try:
#         num_1 = int(input("Enter a number 1\t"))
#         num_2 = int(input("Enter a number 2\t"))
#     except Exception as e:
#         print(Exception)
#     finally:
#         print(num_1)
#
# main()
#
# for temp in range(0,10):
#     print(temp)

# my_string = '03/07/2013'
# list_str = my_string.split('/')
# print(list_str)

# try:
#     x = float('abc123')
#     print(x)
# except IOError:
#     print('This code caused an IOError.')
# except ZeroDivisionError:
#     print('This code caused a ZeroDivisionError.')
# except Exception:
#     print('An error happened.')
# print('The end.')
