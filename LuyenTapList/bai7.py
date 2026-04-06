_list = ['abc', 'xyz', 'abc', '12', 'ii', '12', '5a']

_new_all_removed = [item for item in _list if _list.count(item) == 1]
print("Loại bỏ sạch trùng lặp:", _new_all_removed)

_new_unique = list(dict.fromkeys(_list))
print("Giữ lại 1 bản duy nhất:", _new_unique)