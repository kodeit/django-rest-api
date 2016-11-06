from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserInfoViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserInfoViewSet)

urlpatterns = [
    url(r'^get_token', obtain_auth_token),
    url(r'^', include(router.urls)),
]
