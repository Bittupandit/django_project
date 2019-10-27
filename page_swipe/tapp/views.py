from django.shortcuts import render,get_object_or_404
from tapp.forms import ProductForm,WishlistForm
from .models import Product,Wishlist
from django.http import HttpResponseRedirect

# Create your views here.
def pdt_frm(request):
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save(commit=True)
        return HttpResponseRedirect('/next')
    return render(request,'myapp/main.html',{'form':form})

def pdt_view(request):
    dataitem = Product.objects.all()
    context = {'dataitem':dataitem}
    return render(request,'myapp/next.html',context)

def wishlist_view(request):
    form = WishlistForm(request.POST)
    if form.is_valid():
        items = form.save(commit=True)
        items.save()
        return HttpResponseRedirect('/ss')
    return render(request,'myapp/wishlist.html',{'form':form})

def wishfinal_view(request,id=Product.id):
    items = Wishlist.objects.all()
    context = {'items':items}
    return render(request,'myapp/final.html',context)