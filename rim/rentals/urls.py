from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rent.html$', views.rent, name='rent'),
    url(r'^new_person$', views.new_person, name='new_person'),
    ]

