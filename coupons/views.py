from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import Coupon, Store
from django.shortcuts import redirect

def home(request):
    query = request.GET.get('q')
    if query:
        coupons = Coupon.objects.filter(Q(title__icontains=query) | Q(store__name__icontains=query))
        stores = Store.objects.filter(name__icontains=query)
    else:
        coupons = Coupon.objects.all()
        stores = Store.objects.all()
    return render(request, 'coupons/home.html', {'coupons': coupons, 'stores': stores})

def store_detail(request, slug):
    store = get_object_or_404(Store, slug=slug)
    coupons = Coupon.objects.filter(store=store, is_active=True)
    return render(request, 'coupons/store_detail.html', {'store': store, 'coupons': coupons})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})