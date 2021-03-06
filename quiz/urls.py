from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play, name='play'),
    path('result/<int:total>', views.result, name='result'),
    path('visitorcount/', views.visitor_count, name='visitor_count'),
    path('register_create/', views.register_create_view, name='register_create_view'),
    path('register/', views.register, name='register'),
    path('login/', views.post_login, name='post_login'),
    path('logout/', views.logout, name='logout'),
]

