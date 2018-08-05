from django.conf.urls import include, url
from django.contrib import admin
from GuideApp.views import index

urlpatterns = [
    # Examples:
    # url(r'^$', 'CareerGuide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
]
