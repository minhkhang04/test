# from django.db import models

# class PhanLoai(models.Model):
#     ten = models.CharField(max_length=100)
#     mo_ta = models.TextField()
#     gioi_tinh = models.CharField(max_length=50)
#     mau_sac = models.CharField(max_length=50)

#     def __str__(self):
#         return self.ten

# class SanPham(models.Model):
#     ten = models.CharField(max_length=100)
#     mo_ta = models.TextField()
#     gia_goc = models.DecimalField(max_digits=10, decimal_places=2)
#     gia_sale = models.DecimalField(max_digits=10, decimal_places=2)
#     so_luong = models.PositiveIntegerField()
#     so_luong_ban = models.PositiveIntegerField(default=0)  # Thêm trường số lượng đã bán
#     phan_loai = models.ForeignKey(PhanLoai, on_delete=models.CASCADE, related_name='san_phams')

#     def __str__(self):
#         return self.ten

# class DanhGia(models.Model):
#     san_pham = models.ForeignKey(SanPham, on_delete=models.CASCADE, related_name='danh_gias')
#     khach_hang = models.ForeignKey('KhachHang', on_delete=models.CASCADE, related_name='danh_gias')
#     diem = models.PositiveIntegerField()  # Giả sử điểm số từ 1 đến 5
#     binh_luan = models.TextField(blank=True, null=True)
#     ngay_danh_gia = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f"Đánh giá của {self.khach_hang} cho sản phẩm {self.san_pham}"

# class KhachHang(models.Model):
#     ten = models.CharField(max_length=100)
#     so_dien_thoai = models.CharField(max_length=15)
#     dia_chi = models.TextField()

#     def __str__(self):
#         return self.ten

# class DonHang(models.Model):
#     tong_tien = models.DecimalField(max_digits=12, decimal_places=2)
#     ngay_dat = models.DateField()
#     san_phams = models.ManyToManyField(SanPham, related_name='don_hangs')
#     khach_hangs = models.ManyToManyField(KhachHang, related_name='don_hangs')

#     def __str__(self):
#         return f"Đơn hàng {self.id} - {self.ngay_dat}"

# class Shipper(models.Model):
#     ten = models.CharField(max_length=100)
#     so_dien_thoai = models.CharField(max_length=15)
#     dia_chi = models.TextField()

#     def __str__(self):
#         return self.ten

# class GiaoHang(models.Model):
#     ngay_giao = models.DateField()
#     trang_thai_don_hang = models.CharField(max_length=50)
#     don_hang = models.OneToOneField(DonHang, on_delete=models.CASCADE, related_name='giao_hang')
#     shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, related_name='giao_hangs')

#     def __str__(self):
#         return f"Giao hàng {self.id} - {self.ngay_giao}"
