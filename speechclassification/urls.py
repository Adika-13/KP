"""speechclassification URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
import os
from TC.views import *

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard'), name='home'),
    path('dashboard/', include('dashboard.urls')),
    path('grade/', include('grade.urls')),
    path('audio/', include('audio.urls')),
    path('transcribe/', include('transcribe.urls')),
    path('tugas2/', include('tugas2.urls')),
    path('message/', include('message.urls')),
    path('TC/', include('TC.urls')),
    path('preprocessing/', preprocessing, name='preprocessing'),
    path('checker_page/', checker_page, name='checker_page'),
    path('chooseMethod/', chooseMethod, name='chooseMethod'),
    path('classification/', classification, name='classification'),
    path('clustering/', clustering, name='clustering'),
    path('admin/', admin.site.urls),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
