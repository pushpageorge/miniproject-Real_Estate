from django.shortcuts import redirect, render
from django.contrib import messages

from sellerapp.forms import Property_Form
from sellerapp.models import property

# Create your views here.
def sellerindex(request):
    view=property.objects.all()
    return render(request,'seller/index.html',{'view':view})
    
    
def addproperty(request):
    form=Property_Form()
    if request.method == 'POST':  
        form = Property_Form(request.POST, request.FILES)  
        if form.is_valid():  
            form.save() 
            messages.success(request, 'Added Successfull')

            return redirect('addproperty')
    return render(request,'seller/add_property.html',{'form':form})


def view_property(request):
    view=property.objects.all()
    return render(request,'seller/view_property.html',{'view':view})


def edit_property(request,id):
    employee = property.objects.get(id=id)
    form = Property_Form(instance=employee)

    if request.method == 'POST':
        form = Property_Form(request.POST,request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('seller')

    return render(request,'seller\edit_property.html',{'form':form})


def delete(request,id):
    pro = property.objects.get(id=id)

    if request.method == 'POST':
        property.delete()
        return redirect('seller')

    return render(request,'seller/delete.html',{'pro':pro})