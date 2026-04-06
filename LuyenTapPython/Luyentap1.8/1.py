# Từ điển mã hóa
encode_dict = {'a': '!', 'b': '@', 'c': '#', 'd': '$'}

# Tạo từ điển giải mã (đảo ngược)
decode_dict = {v: k for k, v in encode_dict.items()}


# Hàm mã hóa
def encode(text):
    result = ""
    for char in text:
        if char in encode_dict:
            result += encode_dict[char]
        else:
            result += char 
    return result


# Hàm giải mã
def decode(text):
    result = ""
    for char in text:
        if char in decode_dict:
            result += decode_dict[char]
        else:
            result += char
    return result

text = "abcd xyz"

encoded = encode(text)
decoded = decode(encoded)

print("Văn bản gốc:", text)
print("Mã hóa:", encoded)
print("Giải mã:", decoded)