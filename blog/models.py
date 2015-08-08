# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Entrada(models.Model):
    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering=['-fecha']
        
    imagen = models.CharField(u'URL de la Imagen del Post', max_length=1024,   default="/static/img/skyrim.jpg")
    titulo = models.CharField(u'Título', max_length=100)
    fecha = models.DateTimeField(u'Fecha del Post',auto_now_add=True)
    resumen= models.CharField(u'Resumen',max_length=512)
    contenido = models.TextField(u'Contenido')
    multimedia = models.FileField(u'Multimedia', upload_to='/multimedia', blank=True)
    published = models.BooleanField(u'Habilitado', default=True)
    autor = models.ForeignKey(User)
    tag = models.ManyToManyField('Categoria')
    
    def __str__(self):
        return self.titulo
    
class Contacto(models.Model):
    class Meta:
        verbose_name = "Contacto"
    nombre = models.CharField(u'Nombre',max_length=100)
    mail = models.CharField(u'Mail',max_length=100)
    asunto = models.CharField(u'Asunto',max_length=100)
    mensaje = models.TextField(u'Mensaje')
    
    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(u'Nombre del Tag', max_length=100)
    
    
    def __str__(self):
        return self.nombre
    
class Mensajes(models.Model):
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering=['-fecha']
        
    nombre = models.CharField(u'Nombre', max_length=100)
    mensaje = models.TextField(u'Mensaje')
    published = models.BooleanField(u'Habilitado', default=True)
    fecha = models.DateTimeField(u'Fecha del Mensaje', auto_now_add=True)
    published_in = models.ForeignKey(Entrada)
    
    def __str__(self):
        return self.nombre
