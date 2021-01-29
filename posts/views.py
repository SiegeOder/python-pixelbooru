from django.contrib.auth.models import User
from django.core.paginator import Paginator, Page
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from comments.models import Comment
from .models import Post
from . import forms

Page.next_next = lambda self: self.paginator.validate_number(self.number + 2)
Page.prev_prev = lambda self: self.paginator.validate_number(self.number - 2)
Page.prev_last = lambda self: self.paginator.num_pages - 1
Page.next_num = lambda self: self.paginator.num_pages - self.number


def index(request):
    if 'tags' in request.GET:
        tags = request.GET['tags'].split()
        if tags:
            posts = Post.objects.order_by('-id')
            for tag in tags:
                if tag[0] != '-':
                    posts = posts.filter(tags__name=tag)
                else:
                    posts = posts.exclude(tags__name=tag[1:])
        else:
            posts = Post.objects.order_by('-id')
    else:
        posts = Post.objects.order_by('-id')
    return render(request, 'posts/index.html', {'posts': Paginator(posts, 30).get_page(request.GET.get('page'))})


def view(request, id):
    post = Post.objects.get(id=id)
    tags = post.tags.order_by('type')
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/post.html', {'post': post, 'comments': comments, 'tags': tags})


@login_required(login_url='/signin')
def comment(request, id):
    if request.method == 'POST':
        if text := request.POST['text']:
            Comment.objects.create(
                text=text,
                post=Post.objects.get(id=id),
                author=User.objects.get(id=request.POST['user']).profile
            )
        return redirect('posts:post', id)


@login_required(login_url='/signin')
def create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('posts:index')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/create.html', {'form': form})
