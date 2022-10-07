from django.urls import path
from . import apiREST

urlpatterns = [
    path('ping/', apiREST.ping.as_view()),
    path('pingAuth/', apiREST.pingAuth.as_view()),
    path('account/', apiREST.getAccountList),
]