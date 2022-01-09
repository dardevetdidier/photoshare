from django.shortcuts import render
from .models import Category, Photo


def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories,
               'photos': photos}
    return render(request, 'photos/gallery.html', context=context)


def viewphoto(request, pk):
    photo = Photo.objects.get(pk=pk)
    context = {'photo': photo}
    return render(request, 'photos/photo.html', context=context)


def addphoto(request):
    return render(request, 'photos/add.html')
