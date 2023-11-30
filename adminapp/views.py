from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from Real_estate_app.models import seller_Reg

# Create your views here.
def adminindex(request):
    sell = seller_Reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')

    return render(request,'admin/index.html',{'sell':sell})


def approve(request,id):
    user = User.objects.get(pk=id)
    user.last_name='1'
    user.save()
    messages.success(request, 'Approved Successfull')

    return redirect('admin')
    

def reject(request,id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('admin')

    return render(request,'admin/delete.html',{'user':user})

def seller_list(request):
    seller=seller_Reg.objects.all()

    return render(request,'admin/seller_list.html',{'seller':seller})
