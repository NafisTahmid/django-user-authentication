from django.urls import path
from login import views
app_name = 'login'
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('user_login/', views.user_login, name='user_login')
]
