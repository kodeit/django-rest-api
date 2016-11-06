from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import HelloView, UserFormView

urlpatterns = [
    url(r'^$', UserFormView.as_view()),
    url(r'^hello/', HelloView.as_view()),
    url(r'^api/', include('users.api.urls')),
]
