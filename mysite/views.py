from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.sitemaps import Sitemap




def post_list(request):
    posts = Post()
    return render(request, 'blog/sitemap.xml', {'posts': posts})