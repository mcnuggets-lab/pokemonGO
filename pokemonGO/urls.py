"""pokemonGO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage



urlpatterns = [
    url(r'^pokemonGO/', include('graphs.urls', namespace='pkmg')),
    url(r'^home/', include('home.urls', namespace='home')),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico', RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    url(r'^about/', RedirectView.as_view(url='/home/about/')),
    url(r'^$', RedirectView.as_view(url='/home/')),
]
