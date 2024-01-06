from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.http import HttpResponse


def insert_topic(request):
    ETFO=Topicform()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=Topicform(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']

            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()

            return HttpResponse('data is created.')
        else:
            return HttpResponse('invalid data.')
        
    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    EWFO=Webpageform()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=Webpageform(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            TO=Topic.objects.get(topic_name=tn)
            n=WFDO.cleaned_data['name']
            u=WFDO.cleaned_data['url']
            e=WFDO.cleaned_data['email']

            WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
            WO.save()

            return HttpResponse('data is created.')
        else:
            return HttpResponse('data is invalid.')

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EAFO=Accessrecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            n=AFDO.cleaned_data['name']
            WO=Webpage.objects.get(pk=n)
            a=AFDO.cleaned_data['author']
            d=AFDO.cleaned_data['date']

            AO=Accessrecord.objects.get_or_create(name=WO,author=a,date=d)[0]
            AO.save()

            return HttpResponse('data is created.')
        else:
            return HttpResponse('data is invalid.')

    return render(request,'insert_accessrecord.html',d)