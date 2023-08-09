from django.db import models
from django.contrib.auth.models import AbstractUser

# # funcion para la carga de imagenes de usuario:
# def upload_image(instance, filename):
#     return "img/users/{id}/{filename}".format( id = instance.pk, filename = filename)

# Create your models here.
class User(AbstractUser):
    # Coleccion para los tipos de documento de identidad:
    TIPODOCUMENTO_CHOICES= [
        ("CC","Cédula Ciudadania"),
        ("CE","Cedula Extranjeria"),
        ("TI","Tarjeta Identidad"),
        ("PA","Pasaporte"),
        ("RC","Registro civil"),
        ("NN","No Identificado"),
        ("OTRO","Otro")
    ]
    # Sobreescribo el campo'username':
    email = models.EmailField(verbose_name='Correo Electrónico', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    tipo_id = models.CharField(verbose_name='Tipo de identificación', max_length = 20, choices=TIPODOCUMENTO_CHOICES)
    identification = models.CharField(verbose_name='Número de Identificación', max_length = 20)
    # photo = models.ImageField(verbose_name='Foto de Perfil', upload_to=upload_image, null=True, blank=True)
    country = models.CharField(verbose_name= 'Pais', max_length=255)
    city = models.CharField(verbose_name= 'Ciudad ', max_length=255)
    addres = models.CharField(verbose_name= 'Dirección', max_length=255)
    phone = models.CharField(verbose_name= 'Telefono', max_length=255)
    birthday = models.DateField(verbose_name= 'Fecha de Nacimiento', null=True, blank=True)
    ocupation_job = models.CharField(verbose_name= 'Ocupación', max_length=255)
    relocate = models.BooleanField(verbose_name= 'Se puede Desplazar?', default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)




