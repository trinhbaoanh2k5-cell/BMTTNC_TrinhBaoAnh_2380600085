def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

# Sử dụng eval để nhận dạng cấu trúc tuple khi nhập (ví dụ: 1, 2, 3)
input_tuple = eval(input("Nhập tuple (ví dụ 1, 2, 3): "))
first, last = truy_cap_phan_tu(input_tuple)

print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
