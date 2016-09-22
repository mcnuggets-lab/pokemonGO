from django.conf.urls import url

from . import views

app_name = 'pokemonGO'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^CPvHP/$', views.cpvhp, name='CPvHP')
]