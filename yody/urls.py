"""
URL configuration for yody project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#dùng để khi click qua trang mới thì không bị lỗi khi load ảnh từ API
from django.conf import settings
from django.conf.urls.static import static
# from home.views import get_home 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', get_home, name='home'),  # Định nghĩa đường dẫn trực tiếp đến view get_home
    path('', include('home.urls')),  # Bao gồm các đường dẫn từ ứng dụng home
]

#dùng để khi click qua trang mới thì không bị lỗi khi load ảnh từ API
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)