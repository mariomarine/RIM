from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rent.html$', views.rent, name='rent'),
    url(r'^new_customer$', views.new_customer, name='new_customer'),
    url(r'^thanks.html$', views.thanks, name='thanks'),
    ]

