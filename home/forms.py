from django import forms
from .models import SanPham
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['ten', 'mo_ta', 'gia_goc', 'gia_sale', 'so_luong', 'so_luong_ban', 'phan_loai']

    def clean(self):
        cleaned_data = super().clean()
        so_luong = cleaned_data.get('so_luong')
        so_luong_ban = cleaned_data.get('so_luong_ban')

        if so_luong_ban > so_luong:
            raise forms.ValidationError("Số lượng đã bán không thể lớn hơn số lượng tồn kho.")
#tạo form đăng ký
class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email này đã được sử dụng.")
        return email
 #form đăng ký   
class CustomerLoginForm(AuthenticationForm):
    username = forms.CharField(label='Tên người dùng', max_length=150)
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)