from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='inform_index'),
    
    url(r'^nation1/$', views.nation1, name='inform_nat1'),
    url(r'^nation2/$', views.nation2, name='inform_nat2'),
    url(r'^nation3/$', views.nation3, name='inform_nat3'),
    url(r'^nation4/$', views.nation4, name='inform_nat4'),
    url(r'^nation5/$', views.nation5, name='inform_nat5'),
    url(r'^nation6/$', views.nation6, name='inform_nat6'),
    
    url(r'^nation1/(\d+)/$', views.detail1, name='inform_det1'),
    url(r'^nation2/(\d+)/$', views.detail2, name='inform_det2'),
    url(r'^nation3/(\d+)/$', views.detail3, name='inform_det3'),
    url(r'^nation4/(\d+)/$', views.detail4, name='inform_det4'),
    url(r'^nation5/(\d+)/$', views.detail5, name='inform_det5'),
    url(r'^nation6/(\d+)/$', views.detail6, name='inform_det6')
]