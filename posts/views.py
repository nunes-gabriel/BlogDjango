from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    return render(request, 'post.html', {'post': post})


def criticas(request):
    posts = Post.objects.all()
    return render(request, 'criticas.html', {'posts': posts})


def noticias(request):
    posts = Post.objects.all()
    return render(request, 'noticias.html', {'posts': posts})
