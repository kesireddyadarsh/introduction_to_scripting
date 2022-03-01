import re
print("This is regular expression")
var_1 = """
This is String 12321
 This is String 12321
 This is String 12321
  This is String 12321
  This is String 12321 This is String 12321
  This is String 12321 This is String 12321 This is String 12321 """



student_details = """
User Lastname ulastname@islander.tamucc.edu 100,20,30,40,50,50
Temp User tuser@islander.tamucc.edu 100,20,30,40,50,50
Remo Range rrange@islander.tamucc.edu 100,20,30,40,50,50
Will Rack wrack@islander.tamucc.edu 100,20,30,40,50,50
Tam Smith tsmith@islander.tamucc.edu 100,20,30,40,50,50
Wish Rack wrack@islander.tamucc.edu 100,20,30,40,50,50
"""

find_email = re.findall('[a-z]+@islander.tamucc.edu',student_details)
print(find_email)

test_number = '800-234-2342'
test_number_1 = '800-231-1232'
test_number_2 = '800.231.1232'
#I want to highlight test_number and test_number_1 test_number_2
