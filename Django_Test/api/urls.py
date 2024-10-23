from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.ProductoListCreate.as_view(), name='producto-list'),
    path('productos/<int:pk>/', views.ProductoDetail.as_view(), name='producto-detail'),
    path('clientes/', views.ClientesListCreate.as_view(), name="ventas-list"),
    path('clientes/<int:pk>/', views.VentasDetail.as_view(), name="ventas-detail"),
    path('pedidos/', views.PedidosListCreate.as_view(), name='pedidos-list'),
    path('pedidos/<int:pk>/', views.PedidosDetail.as_view(), name='pedidos-detail'),
    path('ventas/', views.VentasListCreate.as_view(), name= 'ventas-list'),
    path('ventas/<int:pk>/',views.VentasDetail.as_view(), name= 'ventas-detail')
]           

