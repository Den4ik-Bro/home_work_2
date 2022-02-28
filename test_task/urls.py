from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainListView.as_view(), name='main'),
    path('api/main/', views.ListApiTable.as_view(), name='main_api'),
]