from django.urls import path

from . import views
urlpatterns = [

    path('',views.community,name='community'),
    #button
    path('initiate/', views.initiate, name='initiate'),
    path('invest/', views.invest, name='invest'),


]
