from django.conf.urls import url

from .views import UserFormView, HelloView

urlpatterns = [
    url(r'^$', UserFormView.as_view()),
    url(r'^hello/', HelloView.as_view()),
]
