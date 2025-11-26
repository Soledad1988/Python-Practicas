from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False, default='Sin categoria')

    def __str__(self):
         return self.nombre

class Articulo(models.Model):
     titulo = models.CharField(max_length=50, null=False)
     resumen = models.TextField(null=False)
     contenido = models.TextField()
     fecha_publicacion = models.DateField(auto_now_add=True)
     activo = models.BooleanField(default=True)
     categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
     imagen = models.ImageField(null=True, blank=True, upload_to='media', default='articulo_por_defecto.png')
     publicado = models.DateField(default=timezone.now)
  #   editor = models.ForeignKey

class meta:
     ordering = ('-publicado',)

def __str__(self):
         return self.titulo

# Borrado de imágenes
class image(models.Model):
      articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='images')
      image = models.ImageField(null = True, upload_to='articulo', default='articulo/articulo_por_defecto.png')


      def delete(self, using = None, keep_parents = False):
            self.image.delete()
            super().delete(using=using, keep_parents=keep_parents)