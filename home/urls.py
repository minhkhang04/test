# home/urls.py
from django.urls import path
# from .views import get_home ,them_san_pham ,customer_login, customer_register
# from .views import PhanLoaiListAPIViews,SanPhamListAPIView,HinhAnhSPListAPIView
# from .views import DanhGiaListAPIView,KhachHangListAPIView,DonHangListAPIView,ShipperListAPIView,GiaoHangListAPIView
# # Import view từ cùng một ứng dụng
from .views import *
urlpatterns = [
    path('', get_home, name='home'),  # Định nghĩa đường dẫn đến view get_home
    path('add/product',them_san_pham,name='them-san-pham'),
    path('login/', customer_login, name='customer_login'),
    path('tao-don-hang/', tao_don_hang, name='tao_don_hang'),
    path('register/', customer_register, name='customer_register'),
    #API phân loại
    path('listPhanLoai/list',PhanLoaiListAPIViews.as_view(),name='list-phan-loai'),
    path('create/phanloai',PhanLoaiCreateAPIView.as_view(),name='create-phan-loai'),
    path('update/phanloai',PhanLoaiUpdateAPIView.as_view(),name='update-phan-loai'),
    path('delete/phanloai',PhanLoaiDeleteAPIView.as_view(),name='delete-phan-loai'),

    #API sản phẩm
    path('listSP',SanPhamListAPIView.as_view(),name='list-san-pham'),
    path('create/sanpham',SanPhamCreateAPIView.as_view(),name='create-san-pham'),
    path('update/sanpham/<int:pk>/', SanPhamUpdateAPIView.as_view(), name='update-san-pham'),
    path('delete/sanpham/<int:pk>/', SanPhamDeleteAPIView.as_view(), name='delete-san-pham'),

    #API hình ảnh sản phẩm
    path('listHinhAnhSP',HinhAnhSPListAPIView.as_view(),name='list-image-sp'),
    path('create/hinhanhsp',HinhAnhSPCreateAPIView.as_view(),name='create-image-sp'),
    path('update/hinhanhsp',HinhAnhSPUpdateAPIView.as_view(),name='update-image-sp'),
    path('delete/hinhanhsp',HinhAnhSPDeleteAPIView.as_view(),name='delete-image-sp'),

    #API đánh giá sản phẩm
    path('list/DanhGia',DanhGiaListAPIView.as_view(),name='list-dang-gia'),
    path('create/danhGia',DanhGiaCreateAPIView.as_view(),name='create-dang-gia'),
    path('update/danhGia',DanhGiaUpdateAPIView.as_view(),name='update-dang-gia'),
    path('delete/danhGia',DanhGiaDeleteAPIView.as_view(),name='delete-dang-gia'),

    #API khách hàng
    path('list/khach',KhachHangListAPIView.as_view(),name='list-khach'),
    path('create/khach',KhachHangCreateAPIView.as_view(),name='create-khach'),
    path('update/khach',KhachHangUpdateAPIView.as_view(),name='update-khach'),
    path('delete/khach',KhachHangDeleteAPIView.as_view(),name='delete-khach'),

    #API đơn hàng
    path('list/donhang',DonHangListAPIView.as_view(),name='list-don-hang'),
    path('create/donhang',DonHangCreateAPIView.as_view(),name='create-don-hang'),
    path('update/donhang',DonHangUpdateAPIView.as_view(),name='update-don-hang'),
    path('delete/donhang',DonHangDeleteAPIView.as_view(),name='delete-don-hang'),
    #API shipper
    path('list/shipper',ShipperListAPIView.as_view(),name='list-shipper'),
    path('create/shipper',ShipperCreateAPIView.as_view(),name='create-shipper'),
    path('update/shipper',ShipperUpdateAPIView.as_view(),name='update-shipper'),
    path('delete/shipper',ShipperDeleteAPIView.as_view(),name='delete-shipper'),
    #API Giao hàng
    path('list/giaohang',GiaoHangListAPIView.as_view(),name='list-giao-hang'),
    path('create/giaohang',GiaoHangCreateAPIView.as_view(),name='create-giao-hang'),
    path('update/giaohang',GiaoHangUpdateAPIView.as_view(),name='update-giao-hang'),
    path('delete/giaohang',GiaoHangDeleteAPIView.as_view(),name='delete-giao-hang'),
]
