from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # 获取访问令牌和刷新令牌的视图
    TokenRefreshView,      # 使用刷新令牌获取新访问令牌的视图
)

urlpatterns = [
    # 获取JWT令牌接口
    # POST请求，携带username和password，返回access和refresh令牌
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # 刷新JWT令牌接口
    # POST请求，携带refresh令牌，返回新的access令牌
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]