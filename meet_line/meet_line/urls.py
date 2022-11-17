from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .settings import ADMIN_PATH 


urlpatterns = [
    path(ADMIN_PATH, admin.site.urls),
    path('', include('shop.urls'))
]#+ #static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
