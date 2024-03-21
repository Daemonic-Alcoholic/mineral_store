from django.shortcuts import render
from django.views.generic import DetailView

from product.models import Product


# Create your views here.

def product_detail(request, pk):
    template_name = 'product/product_detail.html'
    context = {}
    return render(request, template_name, context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_list.html'
    context_object_name = 'product'
