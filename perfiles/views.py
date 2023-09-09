from datetime import date, datetime
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import User


# Create your views here.
class UserListView(ListView):
    template_name = 'perfiles/user_list.html'
    model = User
    paginate_by = 3

class UserDetailView(DetailView):
    model = User
    template_name = 'perfiles/user_detail.html'
    age_user = 0

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
    
    def get_edad(self, fecha_nacimiento):
        try:
            if datetime.now().month <= fecha_nacimiento.month and datetime.now().day <= fecha_nacimiento.day:
                # Si el mes y el día actual es menor o igual al del nacimiento
                edad = (datetime.now().year-1) - fecha_nacimiento.year
            else:
                edad = datetime.now().year - fecha_nacimiento.year
        except:
            edad = 'No es posible calcular la edad'

        return edad
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        usuario_id = self.kwargs['username']
        data = get_object_or_404(User, username=usuario_id)
        
        links = data.links_set.all()
        excerp = data.excerp_set.all()
        proyectos = data.projectdev_set.all()
        habilidades = data.skills_set.all()
        empleos = data.employmenthistory_set.all()
        hechos = data.facts_set.all()
        usuario_fechanace = data.birthday
        self.age_user = self.get_edad(usuario_fechanace)
        academia = data.academy_set.all()


        contexto['links'] = links
        contexto['excerp'] = excerp
        contexto['academia'] = academia
        contexto['proyectos'] = proyectos
        contexto['habilidades'] = habilidades
        contexto['empleos'] = empleos
        contexto['hechos'] = hechos
        contexto['edad'] = self.age_user

        return contexto
