from django.conf.urls import url
from .views import homeView, logoutView

urlpatterns= [
    url(r'^/logout/', logoutView, name='logout'),
    url(r'^/', homeView, name='home'),
]