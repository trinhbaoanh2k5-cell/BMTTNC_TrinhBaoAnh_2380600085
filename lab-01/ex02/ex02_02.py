# Nhập bán kính từ người dùng
# Dùng float() để cho phép nhập số thập phân (ví dụ: 5.5)
ban_kinh = float(input("Nhập bán kính của hình tròn: "))

# Tính diện tích theo công thức: Diện tích = Pi * r^2
# Trong Python, toán tử ** dùng để tính lũy thừa
dien_tich = 3.14 * (ban_kinh ** 2)

# In kết quả ra màn hình
print(f"Diện tích của hình tròn với bán kính {ban_kinh} là: {dien_tich}")
