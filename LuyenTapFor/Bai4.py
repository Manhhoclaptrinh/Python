n = int(input("Nhập số nguyên n < 20: "))
if n >= 20:
    print("Số nhập vào phải nhỏ hơn 20.")
else:
    for i in range(1, n + 1):
        if i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")