from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  # Anasayfa
    path('login/', views.login_view.as_view(), name='login'),  # Login sayfası
    path('base/', views.BaseView.as_view(), name='base'),  # Base sayfası
]
