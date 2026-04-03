def chia_het_cho_5(so_nhi_phan):
    # Chuyển nhị phân sang thập phân hệ cơ số 2
    so_thap_phan = int(so_nhi_phan, 2)
    return so_thap_phan % 5 == 0

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (cách bởi dấu phẩy): ")
so_nhi_phan_list = chuoi_so_nhi_phan.split(',')

# Lọc các số thỏa điều kiện
ket_qua = [so for so in so_nhi_phan_list if chia_het_cho_5(so)]

if len(ket_qua) > 0:
    print("Các số nhị phân chia hết cho 5 là:", ','.join(ket_qua))
else:
    print("Không có số nào thỏa mãn.")
