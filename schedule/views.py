from django.shortcuts import render
from django.utils import timezone
from .models import Post

def schedule(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'schedule/hi.html', {'posts': posts})