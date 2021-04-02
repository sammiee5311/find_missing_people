from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'web_board'

urlpatterns = [
    url(r'^$', views.Web_board.as_view(), name='web_board'),
    url(r'^request/$', views.check_board, name='web_board_request')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)