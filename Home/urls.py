from django.conf.urls import url
from .views import homeView 

urlpatterns= [
    url(r'^', homeView.as_view(template_name = 'home.html'), name='home'),
]