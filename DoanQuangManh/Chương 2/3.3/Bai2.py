_a = int(input("Nhập cạnh a: "))
_b = int(input("Nhập cạnh b: "))
_c = int(input("Nhập cạnh c: "))

if _a + _b > _c and _a + _c > _b and _b + _c > _a:
    print("Độ dài 3 cạnh tam giác ")
else:
    print("Đây không phải là 3 cạnh của một tam giác")
