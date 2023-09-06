from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import User

# Create your views here.
class UserListView(ListView):
    template_name = 'perfiles/user_list.html'
    model = User
    paginate_by = 6

class UserDetailView(DetailView):
    model = User
