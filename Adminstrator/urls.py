
from django.urls import path
from Adminstrator import views

app_name="Adminstrator"

urlpatterns = [


    path('HomePage/',views.LoadingHomePage,name="LoadingHomePage"),

    path('District/', views.districtInsertSelect,name="districtInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('districtupdate/<int:eid>',views.districtupdate,name="districtupdate"),
    
    path('Category/', views.CategoryInsertSelect,name="CategoryInsertSelect"),
    path('delCategory/<int:did>', views.delCategory,name="delCategory"),
    path('Categoryupdate/<int:eid>',views.Categoryupdate,name="Categoryupdate"),


    path('AdminRegistration/', views.AdminRegistrationInsertSelect,name="AdminRegistrationInsertSelect"),
    path('delAdminRegistration/<int:did>', views.delAdminRegistration,name="delAdminRegistration"),
    path('AdminRegistrationupdate/<int:eid>',views.AdminRegistrationupdate,name="AdminRegistrationupdate"),




    path('Place/', views.placeInsertSelect,name="placeInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('placeupdate/<int:eid>',views.placeupdate,name="placeupdate"),



    
    path('Ewaste/', views.ewasteInsertSelect,name="ewasteInsertSelect"),
    path('delewaste/<int:did>', views.delewaste,name="delewaste"),
    path('ewasteupdate/<int:eid>',views.ewasteupdate,name="ewasteupdate"),
    



    path('UserListNew/',views.userListNew,name="userListNew"),
    path('acceptuser/<int:aid>',views.acceptuser,name="acceptuser"),
    path('rejectuser/<int:rid>',views.rejectuser,name="rejectuser"),
    path('UserListAccepted/',views.userListAccepted,name="userListAccepted"),
    path('UserListRejected/',views.userListRejected,name="userListRejected"),
    

    
    path('Company/',views.company,name="company"),
    path('acceptcmp/<int:aid>',views.acceptcmp,name="acceptcmp"),
    path('rejectcmp/<int:rid>',views.rejectcmp,name="rejectcmp"),
    path('CompanyAccepted/',views.companyAccepted,name="companyAccepted"),
    path('CompanyRejected/',views.companyRejected,name="companyRejected"),

    path('ViewComplaintList/',views.viewcomplaintlist,name="viewcomplaintlist"),
    
    path('Reply/<int:cid>',views.reply,name="reply"),


    path('ViewFeedback/',views.viewfeedback,name="viewfeedback"),
    
]

