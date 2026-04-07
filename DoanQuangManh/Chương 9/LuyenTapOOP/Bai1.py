class HocVien:
    def __init__(self, HoTen, NgaySinh, email, DiaChi, Lop):
        self._HoTen = HoTen
        self._NgaySinh = NgaySinh
        self._email = email
        self._Dia_Chi = DiaChi
        self._Lop = Lop
  
    def showInfo(self):
        print("Họ tên: ", self._HoTen)
        print("Ngày sinh: ", self._NgaySinh)
        print("Email: ", self._email)
        print("Địa chỉ: ", self._Dia_Chi)
        print("Lớp: ", self._Lop)
        
    def changeInfo(self, HoTen = None, NgaySinh = None, email = None, DiaChi = None, Lop = None):
        self._HoTen = HoTen
        self._NgaySinh = NgaySinh
        self._email = email
        self._Dia_Chi = DiaChi
        self._Lop = Lop

if __name__ == "__main__":
    hv1= HocVien("Nguyễn Văn A", "01/01/2000", "nguyenvana@example.com", "123 Đường ABC", "Lớp Python")
    hv1.showInfo()
    hv1.changeInfo(HoTen="Đoàn Quang Mạnh",NgaySinh="15/1/2005", email="Doanmanh152005@gmail.com", DiaChi="456 Đường XYZ", Lop="14.2")
    print("Thông tin sau khi cập nhật:")
    hv1.showInfo()
