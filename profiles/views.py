from django.contrib.auth.models import User
from django.core.paginator import Paginator, Page
from django.shortcuts import render
from posts.models import Post

Page.next_next = lambda self: self.paginator.validate_number(self.number + 2)
Page.prev_prev = lambda self: self.paginator.validate_number(self.number - 2)
Page.prev_last = lambda self: self.paginator.num_pages - 1
Page.next_num = lambda self: self.paginator.num_pages - self.number


def profile(request, id):
    profile = User.objects.get(id=id).profile
    posts = Post.objects.filter(author__id=id).order_by('-id')
    return render(request, 'profiles/profile.html',
                  {'profile': profile, 'posts': Paginator(posts, 30).get_page(request.GET.get('page'))})
