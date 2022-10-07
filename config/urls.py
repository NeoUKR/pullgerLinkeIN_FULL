from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('pullgerMM/', include('pullgerMultiSessionManager__FRONT.urls')),
    path('pullgerMSM/api/', include('pullgerMultiSessionManager__REST.urls')),
    path('pullgerAM/api/', include('pullgerAccountManager__REST.urls')),
    path('pullgerR/com_linkedin/api/', include('pullgerReflection.com_linkedin__REST.urls')),
    path('api/account/', include('pullgerAuthJWT.urls')),
]
