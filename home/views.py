from django.shortcuts import render,redirect
from .forms import SanPhamForm
from rest_framework import generics
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomerRegistrationForm, CustomerLoginForm
from .models import PhanLoai,SanPham,HinhAnhSanPham,DanhGia,KhachHang,DonHang,Shipper,GiaoHang
from .models import *
from .serializer import *
# from .serializer import PhanLoaiSerializer,SanPhamSerializer,HinhAnhSPSerializer,DanhGiaSerializer,KhachHangSerializer,DonHangSerializer#lấy danh sách phân loại bằng API
# from .serializer import ShipperSerializer,GiaoHangSerializer
def get_home(request):
    return render(request,'home.html')

def them_san_pham(request):
    if request.method == 'POST':
        form = SanPhamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('danh_sach_san_pham')
        else:
            # Nếu form không hợp lệ, các lỗi sẽ được đưa vào ngữ cảnh và hiển thị lại cho người dùng
            return render(request, 'them_san_pham.html', {'form': form})
    else:
        form = SanPhamForm()
        return render(request, 'them_san_pham.html', {'form': form})

#đăng ký và đăng nhập cho khách hàng

def customer_register(request):
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_login')  # Chuyển hướng đến trang đăng nhập sau khi đăng ký thành công
    else:
        form = CustomerRegistrationForm()

    return render(request, 'register.html', {'form': form})

def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Thay 'home' bằng tên URL của trang chính sau khi đăng nhập thành công
            else:
                form.add_error(None, 'Tên người dùng hoặc mật khẩu không đúng')
    else:
        form = CustomerLoginForm()

    return render(request, 'login.html', {'form': form})
#API phân loại get,post,put,delete
class PhanLoaiListAPIViews(generics.ListAPIView):
    queryset = PhanLoai.objects.all()
    serializer_class = PhanLoaiSerializer

class PhanLoaiCreateAPIView(generics.CreateAPIView):
    queryset = PhanLoai.objects.all()
    serializer_class = PhanLoaiSerializer

class PhanLoaiUpdateAPIView(generics.UpdateAPIView):
    queryset=PhanLoai.objects.all()
    serializer_class = PhanLoaiSerializer

class PhanLoaiDeleteAPIView(generics.DestroyAPIView):
    queryset=PhanLoai.objects.all()
    serializer_class = PhanLoaiSerializer

#API Sản phẩm get,post,put,delete
class SanPhamListAPIView(generics.ListAPIView):
    queryset=SanPham.objects.all()
    serializer_class = SanPhamSerializer

class SanPhamCreateAPIView(generics.CreateAPIView):
    queryset=SanPham.objects.all()
    serializer_class = SanPhamSerializer

class SanPhamUpdateAPIView(generics.UpdateAPIView):
    queryset=SanPham.objects.all()
    serializer_class=SanPhamSerializer

class SanPhamDeleteAPIView(generics.DestroyAPIView):
    queryset=SanPham.objects.all()
    serializer_class=SanPhamSerializer

#API hình ảnh get,post,put,delete
class HinhAnhSPListAPIView(generics.ListAPIView):
    queryset = HinhAnhSanPham.objects.all()
    serializer_class=HinhAnhSPSerializer

class HinhAnhSPCreateAPIView(generics.CreateAPIView):
    queryset = HinhAnhSanPham.objects.all()
    serializer_class=HinhAnhSPSerializer

class HinhAnhSPUpdateAPIView(generics.UpdateAPIView):
    queryset = HinhAnhSanPham.objects.all()
    serializer_class=HinhAnhSPSerializer

class HinhAnhSPDeleteAPIView(generics.DestroyAPIView):
    queryset = HinhAnhSanPham.objects.all()
    serializer_class=HinhAnhSPSerializer

#API danh gia get,post,put,delete
class DanhGiaListAPIView(generics.ListAPIView):
    queryset = DanhGia.objects.all()
    serializer_class=DanhGiaSerializer

class DanhGiaCreateAPIView(generics.CreateAPIView):
    queryset = DanhGia.objects.all()
    serializer_class=DanhGiaSerializer

class DanhGiaUpdateAPIView(generics.UpdateAPIView):
    queryset = DanhGia.objects.all()
    serializer_class=DanhGiaSerializer

class DanhGiaDeleteAPIView(generics.DestroyAPIView):
    queryset = DanhGia.objects.all()
    serializer_class=DanhGiaSerializer

#API khach hang get,post,put,delete
class KhachHangListAPIView(generics.ListAPIView):
    queryset=KhachHang.objects.all()
    serializer_class=KhachHangSerializer

class KhachHangCreateAPIView(generics.CreateAPIView):
    queryset=KhachHang.objects.all()
    serializer_class=KhachHangSerializer

class KhachHangUpdateAPIView(generics.UpdateAPIView):
    queryset=KhachHang.objects.all()
    serializer_class=KhachHangSerializer

class KhachHangDeleteAPIView(generics.DestroyAPIView):
    queryset=KhachHang.objects.all()
    serializer_class=KhachHangSerializer

#API don hang get,post,put,delete
class DonHangListAPIView(generics.ListAPIView):
    queryset=DonHang.objects.all()
    serializer_class=DonHangSerializer

class DonHangCreateAPIView(generics.CreateAPIView):
    queryset=DonHang.objects.all()
    serializer_class=DonHangSerializer
class DonHangUpdateAPIView(generics.UpdateAPIView):
    queryset=DonHang.objects.all()
    serializer_class=DonHangSerializer
class DonHangDeleteAPIView(generics.DestroyAPIView):
    queryset=DonHang.objects.all()
    serializer_class=DonHangSerializer

#API shipper get,post,put,delete
class ShipperListAPIView(generics.ListAPIView):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer

class ShipperCreateAPIView(generics.CreateAPIView):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer
class ShipperUpdateAPIView(generics.UpdateAPIView):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer

class ShipperDeleteAPIView(generics.DestroyAPIView):
    queryset=Shipper.objects.all()
    serializer_class=ShipperSerializer

#API giao hang get,post,put,delete
class GiaoHangListAPIView(generics.ListAPIView):
    queryset=GiaoHang.objects.all()
    serializer_class=GiaoHangSerializer

class GiaoHangCreateAPIView(generics.CreateAPIView):
    queryset=GiaoHang.objects.all()
    serializer_class=GiaoHangSerializer

class GiaoHangUpdateAPIView(generics.UpdateAPIView):
    queryset=GiaoHang.objects.all()
    serializer_class=GiaoHangSerializer

class GiaoHangDeleteAPIView(generics.DestroyAPIView):
    queryset=GiaoHang.objects.all()
    serializer_class=GiaoHangSerializer

from django.contrib.auth.decorators import login_required

@login_required  # Chắc chắn rằng người dùng đã đăng nhập
def tao_don_hang(request):
    if request.method == 'POST':
        # Logic tạo đơn hàng ở đây
        don_hang = DonHang.objects.create(
            tong_tien=...,  # Tính tổng tiền từ sản phẩm
            ngay_dat=...,   # Ngày đặt
            # Thêm các sản phẩm và khách hàng vào đơn hàng
        )
        return redirect('thanh_cong')  # Redirect đến trang thành công
    else:
        # Xử lý cho GET request
        san_phams = SanPham.objects.all()
        return render(request, 'tao_don_hang.html', {'san_phams': san_phams})