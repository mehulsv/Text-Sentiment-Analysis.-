from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sentiment.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include the authentication URLs
]
