from django.shortcuts import render
from .models import Product

def landing_view(request):
    query = request.GET.get('q', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    products = Product.objects.all()

    # Фильтруем по тексту
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)
    
    # Фильтруем по минимальной цене
    if min_price:
        try:
            products = products.filter(price__gte=float(min_price))
        except ValueError:
            pass

    # Фильтруем по максимальной цене
    if max_price:
        try:
            products = products.filter(price__lte=float(max_price))
        except ValueError:
            pass

    return render(request, 'landing.html', {
        'products': products,
        'query': query,
        'min_price': min_price,
        'max_price': max_price
    })

def about_view(request):
    return render(request, 'about.html')