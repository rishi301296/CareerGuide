from django.conf.urls import url
from .views import loginView

urlpatterns = [
    url(r'^$', loginView.as_view(), name='login'),
]