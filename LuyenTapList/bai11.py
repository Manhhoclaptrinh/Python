_list = ["apple", "banana", "kiwi", "orange", "grapes", "pineapple"]

# Nhập số n từ bàn phím
n = int(input("Nhập độ dài n: "))

# Tìm các từ thỏa mãn
_new_list = [word for word in _list if len(word) > n]

print(f"Các từ có độ dài lớn hơn {n} là: {_new_list}")