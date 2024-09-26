import logging
from django.utils.timezone import now

# Thiết lập logger
logger = logging.getLogger(__name__)

class LogSanPhamMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Kiểm tra xem yêu cầu có phải là truy cập đến sản phẩm hay không
        if request.path.startswith('/san-pham/'):  # Điều chỉnh đường dẫn theo URL của bạn
            logger.info(f"Truy cập sản phẩm: {request.path} - Thời gian: {now()}")

        response = self.get_response(request)
        return response
