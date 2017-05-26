from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^schedule$', views.index, name='schedule_index'),
]