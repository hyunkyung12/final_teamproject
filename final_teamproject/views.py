from django.shortcuts import render
from blog.models import Post

# Create your views here.
def main_view(request):
    return render(request, 'main.html', {})
    

# def home_view(request):
#     posts = Post.objects.all()
#     return render(request, 'home.html', {'posts': posts})