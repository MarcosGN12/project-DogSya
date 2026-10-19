from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Dog, Favorite
from products.models import Product

def home(request):
    dogs = Dog.objects.filter(is_available=True)[:6]
    products = Product.objects.all()[:4]
    return render(request, 'home.html', {'dogs': dogs, 'products': products})

def dog_list(request):
    dogs = Dog.objects.filter(is_available=True)

    # Get filter parameters from GET request
    size = request.GET.get('size')
    life_stage = request.GET.get('life_stage')
    gender = request.GET.get('gender')
    required_space = request.GET.get('required_space')
    continent = request.GET.get('continent')

    if size:
        dogs = dogs.filter(size=size)
    if life_stage:
        dogs = dogs.filter(life_stage=life_stage)
    if gender:
        dogs = dogs.filter(gender=gender)
    if required_space:
        dogs = dogs.filter(required_space=required_space)
    if continent:
        dogs = dogs.filter(continent__icontains=continent)

    return render(request, 'dogs/dog_list.html', {'dogs': dogs})

def dog_detail(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    return render(request, 'dogs/dog_detail.html', {'dog': dog})

@login_required
def favorite_list(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'dogs/favorite_list.html', {'favorites': favorites})

@login_required
def toggle_favorite(request, dog_id):
    dog = get_object_or_404(Dog, id=dog_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, dog=dog)
    if not created:
        favorite.delete()
    return redirect(request.META.get('HTTP_REFERER', 'dogs:home'))