from django.urls import path
from .views import ProfileUserView

urlpatterns =[
    path('profile/', ProfileUserView.as_view(), name = 'perfil'),
]