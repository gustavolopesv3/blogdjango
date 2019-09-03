from django.shortcuts import render

# Create your views here.
from blog.form import PostagemForm
from blog.models import *


def index(request):
  posts = Postagem.objects.all()
  return render(request, 'blog/index.html', locals())
def post(request, id):
  posts = Postagem.objects.get(id = id)
  return render(request, 'blog/postagens.html', locals())