# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .models import Univs, EtcMod
from .forms import ModForm
from django.utils import timezone

def index(request):
    return render(request, 'inform/index.html')

'''
#데이터를 받아서 number에 저장하는 방법을 찾아보세요
#form이나 기타 여러 방법이 있습니다.
#request.body에 있는 정보에 접근하던지 하셔야 해요.
def nation(request):
    number = '100'#temp value
    data = Univs.objects.all().filter(uni_number__contains=number).order_by('uni_number')
    return render(request, 'inform/nations.html', {'data': data})
'''
'''
    고쳐봤습니다. 이렇게 하는게 맞나요?
    아 그리고 nation은 인자를 2개 요구하고, detail은 인자를 3개 요구하는데 왜 그런가요?
'''

def nation(request, var):
    if request.method == "POST":
        var = request.POST.get('var', '')
        
    data = Univs.objects.all().filter(uni_number__contains=var).order_by('uni_number')
    
    return render(request, 'inform/nations.html', {'data': data})


def detail(request, uni_number, var):
    if request.method == "POST":
        var = request.POST.get('var', '')
        
    data = Univs.objects.all().filter(uni_number__exact=var)
    etc = EtcMod.objects.all().filter(school_id__exact=var).order_by('-created_date')
    context = {'data': data, 'etc': etc}
    
    return render(request, 'inform/univs.html', context=context)
    

def etcmod(request, a, b):
    data = EtcMod.objects.all().filter(school_id__exact=b).order_by('-created_date')
    
    if request.method == "POST":
        form = ModForm(request.POST)
        if form.is_valid():
            mod = form.save(commit=False)
            mod.author = request.user
            mod.school_id = b
            mod.created_date = timezone.now()
            mod.save()
            
            return render(request, 'inform/univs.html')
    else:
        form = ModForm()
        
    context = {'form': form, 'data': data}
    
    return render(request, 'inform/etcmod.html', context=context)
    

def etclog(request, a, b):
    data = EtcMod.objects.all().filter(school_id__exact=b).order_by('-created_date')
    
    return render(request, 'inform/etclog.html', {'data': data})