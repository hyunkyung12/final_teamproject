from django.conf.urls import include, url
from django.contrib import admin

from .views import main_view
from .views import home_view

urlpatterns = [
    url(r'^$', main_view, name='main_view'),
    url(r'home/', home_view, name='home_view'),
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('users.urls')),    
    url(r'board/', include('board.urls')),
    url(r'inform/', include('inform.urls')),
    url(r'schedule/', include('schedule.urls')), 
]
