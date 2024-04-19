
from django.urls import path
from Guest import views

app_name="Guest"
urlpatterns = [

   


    path('NewUser/',views.userRegistration,name="userRegistration"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    

    path('Company/',views.cmpRegistration,name="cmpRegistration"),


    path('Login/',views.Login,name="Login"),

    path('',views.index,name="index"),
    

]
