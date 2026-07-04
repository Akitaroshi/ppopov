import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Order, OrderItem

def landing_view(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    query = request.GET.get('q', '')
    
    products = Product.objects.all()
    if selected_category:
        products = products.filter(category__id=selected_category)
    if query:
        products = products.filter(name__icontains=query) | products.filter(description__icontains=query)

    return render(request, 'landing.html', {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'query': query
    })

@login_required
def checkout_view(request):
    """Создание реального заказа в базе данных на основе корзины"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            items = data.get('items', [])
            if not items:
                return JsonResponse({'success': False, 'error': 'Корзина пуста'})
            
            # Создаем пустой заказ
            order = Order.objects.create(user=request.user, total_price=0)
            total = 0
            
            for item in items:
                product = get_object_or_404(Product, id=item['id'])
                qty = int(item['qty'])
                subtotal = product.price * qty
                total += subtotal
                
                # Создаем позицию в заказе
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    price=product.price
                )
                
            order.total_price = total
            order.save()
            return JsonResponse({'success': True, 'order_id': order.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
            
    return JsonResponse({'success': False, 'error': 'Метод запрещен'})

@login_required
def payment_view(request, order_id):
    """Симулятор безопасных платежей ЮKassa"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        order.is_paid = True
        order.status = 'paid'
        order.save()
        return render(request, 'payment_success.html', {'order': order})
    return render(request, 'payment_page.html', {'order': order})