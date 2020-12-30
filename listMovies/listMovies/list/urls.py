from django.urls import path
from . import views
from .views import dashboard, delete_post



urlpatterns = [
    path('home/', views.home, name='list-home'),
    path('add/', views.add, name='add-page'),
    path('', views.connexion, name='login-page'),
    path('AtoZ', views.AtoZ, name='AtoZ-page'),
    path('logout/', views.logoutUser, name='logout-page'),
    path('dashboard/', views.dashboard, name='dashboard-page'),
    path('delete/<int:post_id>/', delete_post),
    
]

