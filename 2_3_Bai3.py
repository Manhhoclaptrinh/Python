a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

print("Tổng =", a + b + c)
print("Tích =", a * b * c)

print("Hiệu (a - b) =", a - b)

if b != 0:
    print("Chia nguyên:", a // b)
    print("Chia dư:", a % b)
    print("Chia chính xác:", a / b)
else:
    print("Không thể chia cho 0")