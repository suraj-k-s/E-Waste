from django.urls import path
from Company import views
app_name="Company"
urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),



    path('RequestList/',views.requestlist,name="requestlist"),
    path('acceptrequest/<int:aid>',views.acceptrequest,name="acceptrequest"),
    path('rejectrequest/<int:rid>',views.rejectrequest,name="rejectrequest"),
    path('RequestListAccepted/',views.requestListAccepted,name="requestListAccepted"),
    path('RequestListRejected/',views.requestListRejected,name="requestListRejected"),


    path('Waste/<int:did>',views.waste,name="waste"),
]