from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # use this for seperate login page.
    # In this project we are using home page as login page.
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
