from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

# 仅限开发阶段使用。生产阶段需要在nginx里配置。
if settings.DEBUG:
    urlpatterns += static(
        '/assets/',
        document_root=settings.BASE_DIR / 'static/frontend/assets'
    )
    urlpatterns += static(
        '/media/',
        document_root=settings.MEDIA_ROOT
    )