from django.shortcuts import render

from app1.models import Movie

def home(request):
    k=Movie.objects.all()
    return render(request,'home.html',{'movie':k})

def add(request):
    if request.method == "POST":
        t=request.POST['t']
        d=request.POST['d']
        y=request.POST['y']
        l=request.POST['l']
        i=request.FILES['i']

        m=Movie.objects.create(title=t,description=d,year=y,language=l,image=i)
        m.save()

        return home(request)
    return render(request,'add.html')

def details(request,m):
    k=Movie.objects.get(id=m)
    return render(request,'details.html',{'movie':k})

def delete(request,m):
    k=Movie.objects.get(id=m)
    k.delete()
    return home(request)

def edit(request,m):
    k=Movie.objects.get(id=m)

    if request.method == "POST":
        k.title=request.POST['t']
        k.description=request.POST['d']
        k.year=request.POST['y']
        k.language=request.POST['l']

        if request.FILES.get('i')==None:
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return home(request)

    return render(request,'edit.html',{'movie':k})