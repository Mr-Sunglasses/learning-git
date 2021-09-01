def reverse_list(list_input):
    return list_input[::-1]

def append_list(list_name,word):
    return list_name.append(word)
my_list = [1,2,3,4,5,9,8,0,36,11]

print(reverse_list(my_list))
append_list(my_list,100)
print(my_list)

