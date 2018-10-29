from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pms/', include('pms.urls')),
    path('admin/', admin.site.urls),
]