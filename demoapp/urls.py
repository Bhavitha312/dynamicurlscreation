from django.urls import path
from demoapp import views
 
urlpatterns = [
    path('index',views.index,name='index'),
    path('sample/<int:id>',views.userid,name=''),
   

    path('sample/<str:name>',views.username,name=''),
   
]