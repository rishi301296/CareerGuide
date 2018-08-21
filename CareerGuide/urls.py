from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'CareerGuide.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^index', include('Home.urls')),
    url(r'^signup', include('SignUp.urls')),
    url(r'^login/', include('Login.urls')),
    url(r'^search/', include('Search.urls')),
    url(r'^adminProfile/', include('Admin.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)