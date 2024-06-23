from django.contrib import admin
from django.urls import path
from APP_Inventario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('', views.index_view, name='index'),  # Página inicial protegida por login
]
