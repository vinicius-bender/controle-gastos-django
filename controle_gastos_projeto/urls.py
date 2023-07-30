from django.contrib import admin
from django.urls import path, include
from controle_gastos_app  import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.signup.as_view(), name='signup'),
    path('cadastrar_transacao/', views.cadastrar_transacao, name='cadastrar_transacao'),
    path('remover_transacao/<int:id>/', views.remover_transacao, name='remover_transacao'),
    path('detalhes_transacao/<int:id>/', views.detalhes_transacao, name='detalhes_transacao'),
    path('listagem/', views.listagem, name='listagem'),
]

urlpatterns += staticfiles_urlpatterns()
