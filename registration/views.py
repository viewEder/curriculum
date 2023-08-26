from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import User, Links, Excerp
from datauser.models import Academy, ProjectDev, Skills, EmploymentHistory, HobbiesExtras, Facts

# Create your views here.
class ProfileUserView(TemplateView):
    # Template:
    template_name = 'registration/profile.html'  
    links = []
    hobbies = []
    academy_list = []
    project_list = []
    skill_list = []
    employment_list = []
    facts_list = []

    def get(self, request, *args, **kwargs): 
        links_user = Links.objects.filter(user = request.user)
        hobbies_user = HobbiesExtras.objects.filter(user = request.user)
        academy_users = Academy.objects.filter(user =request.user)
        project_user = ProjectDev.objects.filter(user = request.user)
        skills_user = Skills.objects.filter(user = request.user)
        employment_user = EmploymentHistory.objects.filter(user = request.user)
        facts_user = Facts.objects.filter(user = request.user)
        
        # Enlaces (links):
        for item in links_user:
            if item.link not in self.links:
                 self.links.append(item.link)
        
        # Hobbies de usuario:
        for hobbies in hobbies_user:
            if hobbies.hobby not in self.hobbies:
                self.hobbies.append(hobbies.hobby)

        # Por Estudios realizados
        for item in academy_users:
            academy = {
                    'id': item.id,
                    'type_degree' : item.type_degree,
                    'academy_name' : item.academy_name,
                    'degree_obtained' : item.degree_obtained,
                    'start_date' : item.start_date,
                    'finish_date' : item.finish_date,
                    'in_progress' : item.in_progress
                }
            
            if academy not in self.academy_list:
                self.academy_list.append(academy)
        
        # Por Proyectos en los que participó:
        for item in project_user:
            project = {
                'id': item.id,
                'stack': item.stack,
                'name_project': item.name_project,
                'resume_project': item.resume_project,
                'url_repo': item.url_repo,
                'year_production': item.year_production,
                'developing': item.developing
            }

            if project not in self.project_list:
                self.project_list.append(project)

        # Por Habilidades de usuario:
        for item in skills_user:
            skill = {
                'id': item.id,
                'skill': item.skill,
                'level': item.level,
                'description': item.description,
            }

            if skill not in self.skill_list:
                self.skill_list.append(skill)

        # Por Empleos de usuario:
        for item in employment_user:
            employment = {
                'id': item.id,
                'stack': item.stack,
                'company': item.company,
                'position': item.position,
                'job_description': item.job_description,
                'start_date': item.start_date,
                'end_date': item.end_date,
                'still_work': item.still_work
            }

            if employment not in self.employment_list:
                self.employment_list.append(employment)

        # Por Hechos de usuario:
        for item in facts_user:
            fact = {
                'id': item.id,
                'fact': item.fact,
                'value': item.value,
            }

            if fact not in self.facts_list:
                self.facts_list.append(fact)


        # Retornamos todos los valores obtenidos en el diccionario de contexto:
        return render(request, self.template_name, context = { 'links': self.links, 
                                                               'academia': self.academy_list,
                                                               'proyectos': self.project_list,
                                                               'habilidades': self.skill_list,
                                                               'empleos': self.employment_list,
                                                               'hechos': self.facts_list
                                                             })
