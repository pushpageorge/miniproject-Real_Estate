from sellerapp import views
from django.urls import path
urlpatterns = [
    path('seller',views.sellerindex,name='seller'),
    path('addproperty',views.addproperty,name='addproperty'),
    path('view_property',views.view_property,name='view_property'),
    path('edit_property/<int:id>',views.edit_property,name='edit_property'),
    path('delete/<int:id>',views.delete,name='delete')

]
