from django.conf.urls import url
from .views import updateDbView,requestsView

urlpatterns = [
    url(r'^/updatedb/', updateDbView, name='updatedb'),
    url(r'^/', requestsView, name='adminRequests'),
]