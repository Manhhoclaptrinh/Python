import math

def tinh_tong_hai_so(a, b):
    return a + b

def tinh_tong_danh_sach(danh_sach):
    tong = 0
    for so in danh_sach:
        tong += so
    return tong

def kiem_tra_snt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def tim_snt_trong_khoang(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if kiem_tra_snt(i):
            ket_qua.append(i)
    return ket_qua

def kiem_tra_so_hoan_hao(n):
    if n <= 0:
        return False
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return tong_uoc == n

def tim_so_hoan_hao_trong_khoang(a, b):
    ket_qua = []
    for i in range(a, b + 1):
        if kiem_tra_so_hoan_hao(i):
            ket_qua.append(i)
    return ket_qua

def menu():
    while True:
        print("\n--- MENU LUYỆN TẬP ---")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng dãy số")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong khoảng [a, b]")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong khoảng [a, b]")
        print("0. Thoát")
        
        chon = input("Mời bạn chọn chức năng (0-6): ")
        
        if chon == '1':
            x = float(input("Nhập số thứ nhất: "))
            y = float(input("Nhập số thứ hai: "))
            print(f"Tổng là: {tinh_tong_hai_so(x, y)}")
            
        elif chon == '2':
            ds = input("Nhập các số cách nhau bởi dấu phẩy: ")
            danh_sach_so = [float(i) for i in ds.split(",")]
            print(f"Tổng dãy số là: {tinh_tong_danh_sach(danh_sach_so)}")
            
        elif chon == '3':
            n = int(input("Nhập số cần kiểm tra: "))
            if kiem_tra_snt(n):
                print(f"{n} là số nguyên tố.")
            else:
                print(f"{n} không phải là số nguyên tố.")
                
        elif chon == '4':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print(f"Các SNT trong khoảng [{a}, {b}] là: {tim_snt_trong_khoang(a, b)}")
            
        elif chon == '5':
            n = int(input("Nhập số cần kiểm tra: "))
            if kiem_tra_so_hoan_hao(n):
                print(f"{n} là số hoàn hảo.")
            else:
                print(f"{n} không phải là số hoàn hảo.")
                
        elif chon == '6':
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            print(f"Các số hoàn hảo trong khoảng [{a}, {b}] là: {tim_so_hoan_hao_trong_khoang(a, b)}")
            
        elif chon == '0':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    menu()