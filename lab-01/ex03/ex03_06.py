def xoa_phan_tu(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False

# Dữ liệu mẫu
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key_to_delete = input("Nhập key cần xóa (a, b, c hoặc d): ")

result = xoa_phan_tu(my_dict, key_to_delete)
if result:
    print("Phần tử đã được xóa. Dictionary hiện tại:", my_dict)
else:
    print("Không tìm thấy key trong Dictionary.")
