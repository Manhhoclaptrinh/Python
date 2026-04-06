_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

# Nhập giá trị độ dài tối thiểu từ bàn phím
min_len = int(input("Nhập độ dài tối thiểu: "))

count = 0
for word in _list:
    # Kiểm tra đồng thời 2 điều kiện
    if len(word) >= min_len and word[0] == word[-1]:
        count += 1

print(f"Số lượng chuỗi thỏa mãn là: {count}")