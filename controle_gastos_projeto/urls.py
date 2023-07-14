from django.contrib import admin
from django.urls import path, include
from controle_gastos_app  import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.signup.as_view(), name='signup')
]
