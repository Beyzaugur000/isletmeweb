from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ana sayfa
    path('login/', views.login_view, name='login'),  # Login işlemi
    path('index2/', views.index2, name='index2'),  # Dashboard (index2)
    path('base/', views.BaseView.as_view(), name='base'),  # Base şablon görünümü
]
