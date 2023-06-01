from django.urls import path
from . import views

urlpatterns = [
    # path('register', views.home, name='home'),
    path('', views.home, name='home'),
    path('all/', views.card, name='card'),
    path('addCard/', views.add_card, name='add_card'),
    path('showAnswer/<int:pk>', views.show_answer, name='show_answer'),
    path('randomCard/', views.random_card, name='random_card'),
]