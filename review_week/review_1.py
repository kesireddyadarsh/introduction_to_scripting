# print("Review week")
# print("\nProblem 5:\n")
# # Problem 5: Find prime numbers
# #            - print prime numbers between 2 and 50 inclusively
# # def findAllPrimes(start, end): #function with defined start and end
# #     for num in range(start, end + 1): ## for a int called num in range from the start to the end plus 1
# #         if num > 1: # if num is greater than 1(since all prime numbers are greater than 1)
# #             for i in range(2, num+1): # and for i in a range of 2 till num plus 1
# #                 if(num == 2): ## if num is two print two
# #                     print(num)
# #                     break ## break the if statement so there aren't extra prints and incorrect numbers
# #                 elif (num % i) == 0: ## if num modulus i is 0,
# #                     break # skip
# #                 else:
# #                     print(num) ## if not, print num
# #                     break ## then break to prevent extra prints
# # findAllPrimes(2,50)
# # cant get it to print 2 for some reason
# for s in range(2,50+1):
#     for j in range(2,s):
#         if(s%j)==0:
#             break
#     else:
#         print(s, end=' ')
# print('\n')


# Function 1 for Problem 5
# - makes the first letter of each word in the string uppercase
def upperCase(string):
    newstring = ""
    split = re.split('\s',string)
    print(split)
    for w in split:
        newstring += w[0].upper()
        newstring += w[1:len(w)].lower() + ' '
    return newstring

# Function 2 for Problem 5
# - removes the spaces from the string
def noSpaces(string):
    newstring = ""
    string = upperCase(string)
    split = re.split('\s',string)
    for w in split:
        newstring += w
    return newstring


# Function 3 for Problem 5
# - replaces all instances of 's' with '$' and removes the first 'the' in the string
def sToCash(string):
    newstring = ""
    string = upperCase(string)
    split = re.split('[sS]',string)
    split = split[:len(split)-1]
    for w in split:
        newstring += w + '$'
    split2 = re.split('\s',newstring)
    del split2[2]
    newstring = ""
    for w in split2:
        newstring += w + ' '
    return newstring


# Function 4 for Problem 5
# - only applies upper case to the non-article words (nouns?)
def selectUpper(string):
    newstring = ""
    split = re.split('\s',string)
    for w in split:
        if w == split[0] or w == split[3] or w == split[6]:
            newstring += w[0].upper()
            newstring += w[1:len(w)] + ' '
        else:
            newstring += w + ' '
    return newstring

# Main function
if __name__ == "__main__":
    print("\nProblem 5:\n")
    str5 = "this is the string for the class"
    print("String 5: " + str5)
    print("1: " + upperCase(str5))
    print("2: " + noSpaces(str5))
    print("3: " + sToCash(str5))
    print("4: " + selectUpper(str5))
