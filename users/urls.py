# 안타깝게도, 이제 이 url path들은 사용되지 않아요..

from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'blog/', include('blog.urls')),
]