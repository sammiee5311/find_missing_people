from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web_main'

urlpatterns = [
    url(r'^$', views.Web_main.as_view(), name='web_main'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Web_main_detail.as_view(), name='web_main_detail')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)