from django.contrib import admin

from blog.models import Autor, Postagem

admin.site.register(Autor)
admin.site.register(Postagem)

# Register your models here.
