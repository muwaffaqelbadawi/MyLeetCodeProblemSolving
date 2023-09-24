my_string = "anviaj"

order_list = list()
reversed_list = list()

for i in range(0, len(my_string)):
    order_list.append(my_string[i])

for i in range(len(my_string)-1, -1, -1):
    reversed_list.append(my_string[i])


print(order_list)
print(reversed_list)

# my_list = []
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list.append("string")
# print(my_list)

""" if not my_list:
    print("list is empty")
else:
    print("list is not empty") """
    
