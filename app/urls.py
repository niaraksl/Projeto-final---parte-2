from django.urls import path
from . import views 

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path("produtos/", views.produtos_list, name="produtos_list"),
    path('create/', views.produto_create, name='produto_create'),
    path('update/<int:id>/', views.produto_update, name='produto_update'),
    path('delete/<int:id>/', views.produto_delete, name='produto_delete'),
    path('about/', views.about, name='about'),
    path('second_visit/', views.second_visit, name='second_visit'),
    path('visit/', views.visit, name='visit'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
