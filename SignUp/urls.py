from django.conf.urls import url
from .views import SignUp

urlpatterns = [
    url(r'^signup/$', SignUp().get_signup, name='signup'),
]