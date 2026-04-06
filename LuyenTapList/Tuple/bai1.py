_tuple = ('a', 'b', 'd', 'e')

# Chuyển sang list để có thể chèn
temp_list = list(_tuple)
temp_list.insert(2, 'c') 

# Chuyển về lại tuple
_new_tuple = tuple(temp_list)
print("Tuple sau khi thêm:", _new_tuple)