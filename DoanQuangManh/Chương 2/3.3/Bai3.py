import time

birth_year = int(input("Nhập năm sinh: "))

x = time.localtime()
current_year = x.tm_year

age = current_year - birth_year

print (f" Năm sinh của bạn là: {birth_year}")
print (f" Tuổi của bạn là: {age}")