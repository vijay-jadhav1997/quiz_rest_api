from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('questions/', include('api.urls')),
    path('res_api/', include('res_api.urls')),
]
