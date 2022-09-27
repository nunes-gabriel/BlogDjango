from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/<int:post_pk>', views.post),
    path('criticas', views.criticas),
    path('noticias', views.noticias),
]
