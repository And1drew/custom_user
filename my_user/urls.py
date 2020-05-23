from django.urls import path
from my_user import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.login_view, name='loginpage'),
    path('logout/', views.logout_view)
]
