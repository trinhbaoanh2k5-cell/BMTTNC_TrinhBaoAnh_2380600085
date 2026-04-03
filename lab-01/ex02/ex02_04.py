# Tạo danh sách rỗng lưu kết quả
j = []

# Duyệt qua các số từ 2000 đến 3200
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))

# In kết quả, ngăn cách bởi dấu phẩy
print(','.join(j))
