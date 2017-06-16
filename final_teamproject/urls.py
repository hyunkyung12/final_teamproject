from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

from .views import main_view
from users.views import profile_view

urlpatterns = [
    url(r'^$', main_view, name='main_view'),
    url(r'blog/', include('blog.urls')),
    url(r'inform/', include('inform.urls')),
    url(r'schedule/', include('schedule.urls')),
    url(r'^accounts/profile/$', profile_view, name='profile'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)