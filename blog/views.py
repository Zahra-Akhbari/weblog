from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post


def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(
        request,
        'blog/home.html',
        context
    )

def post_detail(request, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        status='published'
    )

    context = {
        'post': post
    }

    return render(
        request,
        'blog/post_detail.html',
        context
    )