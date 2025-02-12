from django.shortcuts import render , redirect
from .models import *

# Create your views here.

def index(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )

        return redirect("index")

    queryset = Receipe.objects.all()

    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = Receipe.objects.filter(receipe_name__icontains=search)
        
        
    context = {'receipes':queryset}
    return render(request,"index.html",context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)   
    queryset.delete()
    return redirect("index")


def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("receipe_name")
        receipe_description = data.get("receipe_description")
        receipe_image = request.FILES.get("receipe_image")
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect("index")
    
    context = {'receipe':queryset}


    return render(request,"update_receipes.html",{'receipe':queryset})

def serach(request):
    queryset = Receipe.objects.all()
    if request.GET.get("search"):
        search = request.GET.get("search")
        queryset = Receipe.objects.filter(receipe_name__icontains=search)
    context = {'receipes':queryset}
    return render(request,"Search.html",context)