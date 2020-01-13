from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
   url('^clients/$', views.clients),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)