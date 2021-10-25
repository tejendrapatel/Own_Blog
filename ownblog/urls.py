from django.contrib import admin
from django.urls import path
from resume.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name= 'home'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


