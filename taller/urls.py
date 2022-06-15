from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.initial, name = 'initial'),
    path('initial', views.initial, name = 'initial'),
    #path('validate', views.validate, name = 'validate')
]