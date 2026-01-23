from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    # 管理员后台路由
    path('admin/', admin.site.urls),
    path('',include('web.urls')),
]

# 静态文件路由配置
# 注意：仅限开发阶段使用，生产阶段需要在nginx等Web服务器中配置
if settings.DEBUG:
    # 配置前端静态资源路由，将/assets/路径映射到静态文件目录
    urlpatterns += static(
        '/assets/',
        document_root=settings.BASE_DIR / 'static/frontend/assets'
    )
    # 配置媒体文件路由，将/media/路径映射到媒体文件存储目录
    urlpatterns += static(
        '/media/',
        document_root=settings.MEDIA_ROOT
    )