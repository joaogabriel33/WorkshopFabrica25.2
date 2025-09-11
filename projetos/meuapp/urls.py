from django.urls import path
from . import views
from .views import listar_pessoas, criar_pessoa, deletar_pessoa

urlpatterns = [
    path('', views.home, name='home'),
    path('listar/', listar_pessoas, name='listar_pessoas'),
    path('criar/', criar_pessoa, name='criar_pessoa'),
    path('deletar/', deletar_pessoa, name='deletar_pessoa'),
]