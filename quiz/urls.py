from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play, name='play'),
    path('result/<int:total>', views.result, name='result'),
    path('visitorcount', views.visitor_count, name='visitor_count')
]