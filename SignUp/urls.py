from django.conf.urls import url
from .views import SignUp

urlpatterns = [
    url(r'^signup/$', SignUp.as_view(), name='signup'),
]