_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

temp_list = []
for x in _tuple:
    # Nếu phần tử chưa có trong danh sách tạm thì mới thêm vào
    if x not in temp_list:
        temp_list.append(x)

_new_tuple = tuple(temp_list)
print("Kết quả giữ lại 1 bản duy nhất:", _new_tuple)