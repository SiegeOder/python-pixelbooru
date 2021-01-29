from django.shortcuts import render
from posts.models import Post


def home(request):
    posts = str(Post.objects.count())
    return render(request, 'app/home.html', {'posts': posts})
