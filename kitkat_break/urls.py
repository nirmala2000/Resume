from django.urls import path
from kitkat_break import views


urlpatterns = [
    path('' , views.Login,name='login'),
    path('home',views.home,name='home')
]


    


    

