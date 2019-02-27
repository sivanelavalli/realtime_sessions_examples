from django.shortcuts import render
from django.views.generic import DetailView

from .models import *
def Show(request):
    return render(request,"index.html")

def Find(request):
    name=request.POST.get("t1")
    q=Customer.objects.get(pk=name)
    qs=Vehicle.objects.filter(customer=q)
    return render(request,"new.html",{"data":qs})

class GetBrand(DetailView):
    model = Brand
    template_name = "brand.html"

