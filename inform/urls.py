from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^inform/$', views.index, name='inform_index'),
    
    url(r'^inform/nation1/$', views.nation1, name='inform_nat1'),
    
]