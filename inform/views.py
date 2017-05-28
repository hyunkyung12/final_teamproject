from django.shortcuts import render
from .models import Univs

def index(request):
    return render(request, 'inform/index.html', {})
    
def nation1(request):
    data = Univs.objects.all().filter(uni_number__contains='100').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
def nation2(request):
    data = Univs.objects.all().filter(uni_number__contains='200').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
def nation3(request):
    data = Univs.objects.all().filter(uni_number__contains='300').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
def nation4(request):
    data = Univs.objects.all().filter(uni_number__contains='400').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
def nation5(request):
    data = Univs.objects.all().filter(uni_number__contains='500').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
def nation6(request):
    data = Univs.objects.all().filter(uni_number__contains='600').order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
    
def detail1(request, number):
    return render(request, 'inform/univs.html')
def detail2(request, number):
    return render(request, 'inform/univs.html')
def detail3(request, number):
    return render(request, 'inform/univs.html')
def detail4(request, number):
    return render(request, 'inform/univs.html')
def detail5(request, number):
    return render(request, 'inform/univs.html')
def detail6(request, number):
    return render(request, 'inform/univs.html')
    