"""
URL configuration for backoffice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from clientes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/adicionar/', views.adicionar_cliente, name='adicionar_cliente'),
    path('clientes/listar/', views.listar_clientes, name='listar_clientes'),
    path('maquinas/adicionar/', views.adicionar_maquina, name='adicionar_maquina'),
    path('maquinas/listar/', views.listar_maquinas, name='listar_maquinas'),
    path('clientes/buscar/', views.buscar_clientes, name='buscar_clientes'),
    path('clientes/<int:cliente_id>/',
         views.visualizar_cliente, name='visualizar_cliente'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registrar/', views.registrar, name='registrar'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
