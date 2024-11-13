from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', include('results.urls')),  # Includes URLs from the `results` app
]
