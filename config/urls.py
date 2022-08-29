from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pullgerMM/', include('pullgerMultisessionManager_FRONT.urls')),
    path('pullgerStudio/', include('pullgerStudio.urls')),
    path('pullgerMM/api/', include('pullgerMultisessionManager_REST.urls')),
    path('api/account/', include('pullgerAuthJWT.urls')),
]
