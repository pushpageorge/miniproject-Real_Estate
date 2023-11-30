from django.shortcuts import render
from sellerapp.models import property

# Create your views here.
def userindex(request):
    pro=property.objects.all()

    return render(request,'user/index.html',{'pro':pro})

def singleview(request,id):
    singleview=property.objects.get(id=id)

    return render(request,'user/single_view.html',{'singleview':singleview})