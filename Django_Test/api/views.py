from rest_framework import generics
from .models import Producto,Clientes,Pedidos,Ventas
from .serializer import ProductoSerializer,ClientesSerializer,PedidosSerializer,VentasSerializer


# metodos productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


#metodos clientes
class ClientesListCreate(generics.ListCreateAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
    
    
class ClientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer


#metodo pedidos
class PedidosListCreate(generics.ListCreateAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer
    
class PedidosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedidos.objects.all()
    serializer_class = PedidosSerializer

#metodos ventas

class VentasListCreate(generics.ListCreateAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer

class VentasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ventas.objects.all()
    serializer_class = VentasSerializer