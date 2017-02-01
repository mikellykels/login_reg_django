from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.create),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout)
]
