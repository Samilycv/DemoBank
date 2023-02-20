from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('branches/', views.branches, name='branches'),
    path('application/', views.application, name='application'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('dash_board/',views.dashboard, name='dashboard'),
]
