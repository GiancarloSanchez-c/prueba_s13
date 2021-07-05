from django.contrib import admin
from .models import Docente,Alumno,Curso,Notas,Asistencia

# Register your models here.
@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display=['id','firts_name','last_name','name','sexo','date_birth']
    
@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display=['id','firts_name','last_name','name','sexo','date_birth']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display=['id','name','docente']
    
@admin.register(Notas)
class NotasAdmin(admin.ModelAdmin):
    list_display=['id','curso','alumno','nota_1','nota_2','nota_3','nota_4']    

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display=['id','alumno','curso','name']