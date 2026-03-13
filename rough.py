# # lst = [1,2,3]

# # my_str = "mlops playlist"

# # my_int = 155

# # print(type(lst))
# # print(type(my_str))
# # print(type(my_int))

# # print(my_str.upper())

# # a = "x"
# # b = "y"

# # print(a+b)

from oops_proj import chatbook

# # Calling methods
user1 = chatbook()
print(user1.id)

# Using static method directly from class without creating an object
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)


#getter and setter methods
# print(user1.get_name())  
# user1.set_name("Agent X")

# print(user1.get_name())

# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

