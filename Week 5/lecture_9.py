phonebook = {
'Chris' : '555-111',
'Katie' : '231-451',
'Joanne' : '234-124'
}
# temp = phonebook.get('Jill','Not in dictionary')
# print(temp)

# print(phonebook['Chris'])
# if 'Kati' in phonebook:
#     print('In the phonebook')

# for key, value in phonebook.items():
#     print(key, value)
#
# test = phonebook.popitem()
# print(test)
# print(phonebook)
#
# # del phonebook['Chris']
# # print(phonebook)
#
# if 'Chris' in phonebook:
#     print(phonebook['Chris'])
# phonebook['Joe'] = '449-384'
#
# method_dict = dict({1:"class",2:"on",3:"dictionary"})
# print(method_dict)
#
# list_dict = dict([(1,"class"),(2,"list"),(3,"into"),(4,"dictionary")])
# print(list_dict)
#
# name_dict = {"name":{"first_name":"adarsh","last_name":"kesireddy"},
#             "office_hours":"10 to 11"}
# print(name_dict["name"]["first_name"])
#
# class name_dict_c(object):
#     def __init__(self, first_name,last_name,office_hours):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.office_hours = office_hours
#
# test_name = name_dict_c("adarsh","k","1209341")

set_1 = set([1,2,3,4])
set_2 = set([3,4,5,6])
set_3 = set_1.symmetric_difference(set_2)
print(set_3)
