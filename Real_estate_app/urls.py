
from Real_estate_app import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('reg',views.reg,name='reg'),
    path('login',views.loginview,name='login'),
    path('user_registration',views.user_registration,name='user_registration')
]
