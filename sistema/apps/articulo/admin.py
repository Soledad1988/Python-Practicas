from django.contrib import admin
from .models import Categoria, Articulo
# Register your models here.

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'resumen')

admin.site.register(Categoria)

