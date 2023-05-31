from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.card, name='card'),
    path('addCard/', views.add_card, name='add_card'),
    path('showAnswer/<int:pk>', views.show_answer, name='show_answer'),
    path('randomCard/', views.random_card, name='random_card'),
]