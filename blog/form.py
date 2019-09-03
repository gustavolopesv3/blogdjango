from django.forms import ModelForm

from blog.models import Postagem


class PostagemForm(ModelForm):
    class Meta:
        model = Postagem
        fields =  '__all__'