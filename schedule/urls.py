from django.conf.urls import url
from schedule import views

urlpatterns = [
    # name='hi'로 설정하는 것은 바람직하지 않습니다.
    url(r'^$', views.schedule, name='hi'),
]