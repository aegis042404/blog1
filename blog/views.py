from django.shortcuts import render
from django.utils import timezone
from .models import Post #import each model from models.py (ex.01) 
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')#this is a query set, it filters data out of the database and choses the criteria to sort it ex.02
    return render(request, 'blog/post_list.html', {'posts': posts})#ex03

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
