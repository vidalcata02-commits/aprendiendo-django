from django.db import models

# Create your models here.

#colocar los nombres de las entidades en singular

class Article(models.Model): #Entidad

    #propiedades *** Documentar cada tipo de dato
    title = models.CharField(max_length=100)
    content = models.TextField()
    public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model): #Entidad
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created_at = models.DateField()