from adminapp import views
from django.urls import path
urlpatterns = [
    path('admin',views.adminindex,name='admin'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('seller_list',views.seller_list,name='seller_list'),

]
