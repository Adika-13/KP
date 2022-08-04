from django.urls import path

from . import views

app_name = 'TC'

urlpatterns = [
    path('', views.preprocessing, name='preprocessing'),
    path('clustering/', views.clustering, name='clustering'),
    path('classification/', views.classification, name='classification'),
    path('checker_page/', views.checker_page, name='checker_page'),
    path('chooseMethod/', views.chooseMethod, name='chooseMethod')
    
]