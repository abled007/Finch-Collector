from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('finch/', views.FinchList.as_view(), name="finch-list"),
    path('finch/new/', views.Finch_Create.as_view(), name='finch_create'),
    path('finches/<int:pk>/', views.FinchDetail.as_view(), name="finch_detail"),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name="finch_update"),
    path('finches/<int:pk>delete', views.FinchDelete.as_view(), name="finch_delete"),
    path('user/<username>/', views.profile, name='profile'),
    path('finchtoy/', views.finchtoy_index, name='finchtoy_index'),
    path('finchtoy/<int:finchtoy_id>', views.finchtoy_show, name='finchtoy_show'),
    path('finchtoy/create/', views.FinchToyCreate.as_view(), name='finchtoy_create'),
    path('finchtoy/<int:pk>/update/', views.FinchToyUpdate.as_view(), name='finchtoy_update'),
    path('finchtoy/<int:pk>/delete/', views.FinchToyDelete.as_view(), name='finchtoy_delete'),  
]
