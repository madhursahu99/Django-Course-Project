"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from app1.forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'), #url for the login
    url(r'^logout/$', auth_views.logout, {'next_page': 'app1:logout'}, name='logout'), #url for the logout, redirect to logout view
	url(r'^admin/', admin.site.urls), #django built-in admin
    url(r'^', include('app1.urls')),    #url for the site
    url(r'^oauth/', include('social_django.urls', namespace='social')), # url for social media integration
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
