from django.shortcuts import render
from django.views.generic.list import  ListView
from django.views.generic.detail import DetailView
from django.db.models import Q
from .models import Product

# Create your views here.

#LISTANDO LOS PRODUCTOS PARA VERLOS EN EL INDEX
class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listado de productos'
        #context['products'] = context['product_list']
        return context
    

    pass

# CLASE PARA PODER VER EL DETALLE DE LOS PRODUCTOS
class ProductDetailViews(DetailView): #id -> pk
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
    pass

#CLASE PARA PODER VER LOS PRODUCTOS AL BUSCARLOS.
class ProductSearchListViews(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):
        filters = Q(titulo__icontains=self.query()) | Q(category__titulo__icontains=self.query())
        return Product.objects.filter(filters)

    def query (self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count()
        return context
    