from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='inform_index'),
    
    url(r'^(\d+)/$', views.nation, name='inform_nat'),
    
    url(r'^(\d+)/(\d+)/$', views.detail, name='inform_det'),
]