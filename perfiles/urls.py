from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns =[
    path('profiles/', UserListView.as_view(), name = 'usuarios'),
    path('profile/<int:pk>', UserListView.as_view(), name = 'usuario'),
]