from django.urls import path
from .views import produto_create, produto_delete, home, produto_update

app_name = 'app'

urlpatterns = [
    path('', home, name='home'),
    path('create/', produto_create, name='produto_create'),
    path('update/<int:id>/', produto_update, name='produto_update'),
    path('delete/<int:id>/', produto_delete, name='produto_delete'),
]
