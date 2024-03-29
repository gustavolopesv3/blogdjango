from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('index/', views.index, name = 'index'),
    path('post/<int:id>/', views.post, name = 'post'),
    path('about/',views.about, name = 'about'),
    path('contact/',views.contact, name = 'contact')
]
