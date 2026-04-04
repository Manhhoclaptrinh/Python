_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

# Chỉ giữ lại những phần tử có số lần xuất hiện đúng bằng 1
_new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)

print("Kết quả loại bỏ sạch trùng lặp:", _new_tuple)