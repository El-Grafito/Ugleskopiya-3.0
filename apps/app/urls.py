from django.urls import path

from .views import main, user, users, category, profil, info, nazvanie_funk, post_delete, post_edit

urlpatterns = [
    path('', main, name='main'),
    path('user/<username>', user, name='user'),
    path('users/', users, name='users'),
    path('category/<slug>', category, name='category'),
    path('profil', profil, name='profil'),
    path('info', info, name='info'),
    path('edit_profil', nazvanie_funk, name='edit_profil'),
    path('delete_post/<pk>', post_delete, name='post_delete'),
    path('edit_post/<pk>', post_edit, name='post_edit'),

]

