from rest_framework import serializers
#from .models import PhanLoai,SanPham,HinhAnhSanPham,DanhGia,KhachHang,DonHang,Shipper,GiaoHang
from .models import *

class PhanLoaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhanLoai
        fields = '__all__'

class SanPhamSerializer(serializers.ModelSerializer):
    class Meta:
        model=SanPham
        fields='__all__'

class HinhAnhSPSerializer(serializers.ModelSerializer):
    class Meta:
        model = HinhAnhSanPham
        fields = '__all__'

class DanhGiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DanhGia
        fields='__all__'
class KhachHangSerializer(serializers.ModelSerializer):
    class Meta:
        model=KhachHang
        fields='__all__'

class DonHangSerializer(serializers.ModelSerializer):
    class Meta:
        model=DonHang
        fields='__all__'

class ShipperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shipper
        fields='__all__'

class GiaoHangSerializer(serializers.ModelSerializer):
    class Meta:
        model=GiaoHang
        fields='__all__'