from django.urls import path
from myapp import views
 
urlpatterns = [
    path('display',views.display,name='display'),
   
]