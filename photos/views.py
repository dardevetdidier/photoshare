from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


from .models import Category, Photo


def gallery(request):
    category = request.GET.get('category')
    if category is None:
        photos = Photo.objects.all()

    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories,
               'photos': photos,
               }
    return render(request, 'photos/gallery.html', context=context)


def viewphoto(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context=context)


def addphoto(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(pk=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'photos/add.html', context=context)


def login_user(request):
    login_form = LoginForm()
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return redirect('gallery')
        else:
            messages.info(request, "Erreur dans le nom d'utilisateur et/ou le mot de passe")
    return render(request, 'photos/login.html', context={'login_form': login_form})


def logout_user(request):
    logout(request)
    return redirect('gallery')
