from django.urls import path

from .views import user_login, user_signup, logout_cheta

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_signup, name='register'),
    path('logout', logout_cheta, name='logout'),
]

