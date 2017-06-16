from django.conf.urls import url
from inform import views

urlpatterns = [
    url(r'^$', views.index, name='inform_index'),
    url(r'^(\d+)/$', views.nation, name='inform_nat'),
    url(r'^(\d+)/(\d+)/$', views.detail, name='inform_det'),
    url(r'^(\d+)/(\d+)/mod/$', views.etcmod, name='inform_mod'),
    url(r'^(\d+)/(\d+)/log/$', views.etclog, name='inform_log'),
]