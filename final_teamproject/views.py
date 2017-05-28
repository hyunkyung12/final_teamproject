from django.shortcuts import render

# Create your views here.
def main_view(request):
    return render(request, 'main.html', {})
    

def home_view(request):
    return render(request, 'home.html')