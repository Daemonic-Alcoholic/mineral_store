from django.shortcuts import render


# Create your views here.

def product_detail(request, pk):
    template_name = 'product/product_detail.html'
    context = {}
    return render(request, template_name, context)


def product_list(request):
    template_name = 'product/product_list.html'
    context = {}
    return render(request, template_name, context)
