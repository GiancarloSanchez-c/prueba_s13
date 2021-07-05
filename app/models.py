from django.db import models
from django.db import models
from django.contrib.auth.models import User
from .choices import sexos, asistencia

# Create your models here.   
class Docente(models.Model):
    id=models.AutoField(primary_key=True)
    firts_name=models.CharField(max_length=50, blank=False, verbose_name="Apellido Paterno")
    last_name=models.CharField(max_length=50, blank=False, verbose_name="Apellido Materno")
    name=models.CharField(max_length=50, blank=False, verbose_name="Nombres")
    date_birth=models.DateField(verbose_name="Fecha de Nacimiento")
    sexo=models.CharField(max_length=1, choices=sexos, default='M')
    class Meta:
        
        db_table='docente'
        verbose_name='docente'
        verbose_name_plural="docentes"
        ordering = ['id']
    
    def name_complete(self):
        return f'{self.firts_name} {self.last_name}, {self.name}'
    
    def __str__(self):
        return self.name_complete()
    
class Alumno(models.Model):
    id = models.AutoField(primary_key=True)
    firts_name=models.CharField(max_length=50, blank=False, verbose_name="Apellido Paterno")
    last_name=models.CharField(max_length=50, blank=False, verbose_name="Apellido Materno")
    name=models.CharField(max_length=50, blank=False, verbose_name="Nombres")
    date_birth=models.DateField(verbose_name="Fecha de Nacimiento")
    sexo=models.CharField(max_length=1, choices=sexos, default='M') 
    class Meta:
        
        db_table='alumno'
        verbose_name='alumno'
        verbose_name_plural="alumnos"
        ordering = ['id']
    
    def name_complete(self):
        return f'{self.firts_name} {self.last_name}, {self.name}'
    
    def __str__(self):
        return self.name_complete()
    
class Curso(models.Model):
    
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50, blank=False,verbose_name='Nombre del curso')
    docente=models.ForeignKey(Docente, on_delete=models.CASCADE)
    class Meta:
        
        db_table='cursos'
        verbose_name='curso'
        verbose_name_plural="cursos"
        ordering = ['id']
        
    def __str__(self):
        return self.name

class Notas(models.Model):
    id = models.AutoField(primary_key=True)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota_1=models.IntegerField(verbose_name='Nota 1')
    nota_2=models.IntegerField(verbose_name='Nota 2')
    nota_3=models.IntegerField(verbose_name='Nota 3')
    nota_4=models.IntegerField(verbose_name='Nota 4')
    
    class Meta:
        
        db_table='notas'
        verbose_name='nota'
        verbose_name_plural="notas"
        ordering = ['id']
    
    def __str__(self):
        return f'Nota 1: {self.nota_1}, Nota 2: {self.nota_2}, Nota:3: {self.nota_3}, Nota 4: {self.nota_4}' 

class Asistencia(models.Model):
    id = models.AutoField(primary_key=True)
    alumno=models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, choices=asistencia, default='Asistió')
    
    class Meta:
        
        db_table='asistencia'
        verbose_name='asistencia'
        verbose_name_plural="asistencias"
        ordering = ['id']
    
    def __str__(self):
        return self.name