n = int(input("Nhập n: "))

if n < 2:
    print("Không phải số nguyên tố")
else:
    i = 2
    is_prime = True

    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Đây là số nguyên tố")
    else:
        print("Không phải số nguyên tố")