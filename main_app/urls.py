from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finch/', views.FinchList.as_view(), name="finch-list"),
    path('finch/new/', views.Finch_Create.as_view(), name='finch_create'),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
]
