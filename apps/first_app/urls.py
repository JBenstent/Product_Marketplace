from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_product$', views.add_product),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\d+)$', views.product),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^remove/(?P<id>\d+)$', views.remove)
]
