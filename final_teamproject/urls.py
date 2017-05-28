from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from .views import main_view
from .views import home_view

urlpatterns = [
    url(r'^$', main_view, name='main_view'),
    url(r'home/', home_view, name='home_view'),
    url(r'^admin/', admin.site.urls),
    url(r'users/', include('users.urls')),    
    url(r'blog/', include('blog.urls')),
    url(r'inform/', include('inform.urls')),
    url(r'schedule/', include('schedule.urls')), 
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
