
from django.urls import path

from userapp import views
urlpatterns = [
    path('user',views.userindex,name='user'),
    path('singleview/<int:id>',views.singleview,name='singleview'),

]