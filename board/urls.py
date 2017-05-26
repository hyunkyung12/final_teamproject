from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^board/$', views.index, name='board_index'),
]