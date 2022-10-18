from django.shortcuts import render
from numpy import tile
from .models import Product,Order
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    pobj=Product.objects.all()

    #search code
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        pobj=pobj.filter(title__icontains=item_name)

    #paginator

    pag=Paginator(pobj,4)
    page=request.GET.get('page')
    pobj=pag.get_page(page)

    return render(request,'shop/index.html',{'pobj':pobj})

def detail(request,id):
    pobj=Product.objects.get(id=id)

    return render(request,'shop/detail.html',{'pobj':pobj})

def checkout(request):
    if request.method=='POST':
        items=request.POST.get('items','')
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip=request.POST.get('zip','')
        total=request.POST.get('total','')
        order=Order(name=name,email=email,address=address,city=city,state=state,zip=zip,items=items,total=total)
        order.save()
    return render(request,'shop/checkout.html')