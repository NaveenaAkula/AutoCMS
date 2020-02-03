from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    VechicleDeleteView,
    VechicleDetailView,
    VechicleListView,
    VechicleUpdateView,
    VechicleCreateView,


    )


urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/comment/', views.comment, name='comment'),
    path('<int:pk>/vechicle/edit/',
         VechicleUpdateView.as_view(), name='vechicle_edit'),
    path('<int:pk>/vechicle',
         VechicleDetailView.as_view(), name='vechicle_detail'),
    path('<int:pk>/vechicle/delete/',
         VechicleDeleteView.as_view(), name='vechicle_delete'),
    path('vechicle/new/', VechicleCreateView.as_view(), name='vechicle_new'),
    path('vechicle/', VechicleListView.as_view(), name='vechicle_list'),


    # path('send_mail/', SendMail.as_view(), name='sendmail'),
    path('change_password/', views.change_password, name='change_password'),


]
