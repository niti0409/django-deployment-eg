# from django.conf.urls import path
from basic_app import views
from django.urls import path

#TEMPLATE TAGGING
app_name = 'basic_name'

urlpatterns = [
    path('relative/',views.relative,name = 'relative'),
    path('other/',views.other,name = 'other'),
]
