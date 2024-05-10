from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Frontend.urls')),
    # path('api/', include(router.urls)),
    path('api/', include('api.urls')),
]
