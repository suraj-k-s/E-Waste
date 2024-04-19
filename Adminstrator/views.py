from django.shortcuts import render,redirect
from Adminstrator.models import *
from Guest.models import *
from User.models import *
# Create your views here.

def LoadingHomePage(request):
    return render(request,"Adminstrator/HomePage.html")

def ajaxplace(request):
    districtdata=tbl_district.objects.get(id=request.GET.get('disd'))
    placedata=tbl_place.objects.filter(district=districtdata)
    return render(request,"Adminstrator/Ajaxplace.html",{'data':placedata})


def districtInsertSelect(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_district.objects.create(district_name=disName)
        return redirect("Adminstrator:districtInsertSelect")
    else:
        return render(request,"Adminstrator/District.html",{'data':dis})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Adminstrator:districtInsertSelect")

def districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=request.POST.get("txtname")
        editdata.save()
        return redirect("Adminstrator:districtInsertSelect")
    else:
        return render(request,"Adminstrator\District.html",{"editdata":editdata})

    

def CategoryInsertSelect(request):
    dis=tbl_Category.objects.all()
    if request.method=="POST":
        disName=request.POST.get('txtname')
        tbl_Category.objects.create(Category_name=disName)
        return redirect("Adminstrator:CategoryInsertSelect")
    else:
        return render(request,"Adminstrator/Category.html",{'data':dis})

def delCategory(request,did):
    tbl_Category.objects.get(id=did).delete()
    return redirect("Adminstrator:CategoryInsertSelect")

def Categoryupdate(request,eid):
    editdata=tbl_Category.objects.get(id=eid)
    if request.method=="POST":
        editdata.Category_Name=request.POST.get("txtname")
        editdata.save()
        return redirect("Adminstrator:CategoryInsertSelect")
    else:
        return render(request,"Adminstrator\Category.html",{"editdata":editdata})


def AdminRegistrationInsertSelect(request):
    adm=tbl_adminregistration.objects.all()
    if request.method=="POST":
        admName=request.POST.get('txtname')
        admContact=request.POST.get('txtcontact')
        admEmail=request.POST.get('txtemail')
        admPassword=request.POST.get('txtpassword')
        tbl_adminregistration.objects.create(AdminRegistration_name=admName,AdminRegistration_contact=admContact,AdminRegistration_email=admEmail,AdminRegistration_password=admPassword)
        return redirect("Adminstrator:AdminRegistrationInsertSelect")  
    else:
         return render(request,"Adminstrator/AdminRegistration.html",{'data':adm})

def delAdminRegistration(request,did):
    tbl_adminregistration.objects.get(id=did).delete()
    return redirect("Adminstrator:AdminRegistrationInsertSelect")  


def AdminRegistrationupdate(request,eid):
    editdata=tbl_adminregistration.objects.get(id=eid)
    if request.method=="POST":
        editdata.AdminRegistration_name=request.POST.get("txtname")
        editdata.AdminRegistration_contact=request.POST.get("txtname")
        editdata.AdminRegistration_email=request.POST.get("txtname")
        editdata.AdminRegistration_password=request.POST.get("txtname")
        editdata.save()
        return redirect("Adminstrator:AdminRegistartionInsertSelect")
    else:
        return render(request,"Adminstrator\AdminRegistration.html",{"editdata":editdata})




def ewasteInsertSelect(request):
    ewaste=tbl_ewaste.objects.all()
    if request.method=="POST":
        tbl_ewaste.objects.create(ewaste_name=request.POST.get("txtname"),ewaste_details=request.POST.get("txtdetails"),ewaste_price=request.POST.get("txtprice"),ewaste_photo=request.FILES.get("fileImage"))
        return redirect("Adminstrator:ewasteInsertSelect")
    else:
        return render(request,"Adminstrator/Ewaste.html",{'data':ewaste})

def delewaste(request,did):
    tbl_ewaste.objects.get(id=did).delete()
    return redirect("Adminstrator:ewasteInsertSelect")

def ewasteupdate(request,eid):
    editdata=tbl_ewaste.objects.get(id=eid)
    if request.method=="POST":
        editdata.ewaste_name=request.POST.get("txtname")
        editdata.ewaste_details=request.POST.get("txtdetails")
        editdata.ewaste_price=request.POST.get("txtprice")
        editdata.save()
        return redirect("Adminstrator:ewasteInsertSelect")
    else:
        return render(request,"Adminstrator\Ewaste.html",{"editdata":editdata})



  
def Place(request):
    return render(request,"Adminstrator/Place.html")

def userListNew(request):
    userdata = tbl_user.objects.filter(user_status=0)
    return render(request,"Adminstrator/UserListNew.html",{"userdata":userdata})

def acceptuser(request,aid):
    user = tbl_user.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("Adminstrator:LoadingHomePage")

def rejectuser(request,rid):
    user = tbl_user.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("Adminstrator:LoadingHomePage")

def userListAccepted(request):
    userdata = tbl_user.objects.filter(user_status=1)
    return render(request,"Adminstrator/UserListAccepted.html",{"userdata":userdata})

def userListRejected(request):
    userdata = tbl_user.objects.filter(user_status=2)
    return render(request,"Adminstrator/UserListRejected.html",{"userdata":userdata})


def company(request):
    cmpdata = tbl_company.objects.filter(cmp_status=0)
    return render(request,"Adminstrator/Company.html",{"cmpdata":cmpdata})

def acceptcmp(request,aid):
    cmp = tbl_company.objects.get(id=aid)
    cmp.cmp_status = 1
    cmp.save()
    return redirect("Adminstrator:LoadingHomePage")

def rejectcmp(request,rid):
    cmp = tbl_company.objects.get(id=rid)
    cmp.cmp_status = 2
    cmp.save()
    return redirect("Adminstrator:LoadingHomePage")

def companyAccepted(request):
    cmpdata = tbl_company.objects.filter(cmp_status=1)
    return render(request,"Adminstrator/CompanyAccepted.html",{"cmpdata":cmpdata})

def companyRejected(request):
    cmpdata = tbl_company.objects.filter(cmp_status=2)
    return render(request,"Adminstrator/CompanyRejected.html",{"cmpdata":cmpdata})



def placeInsertSelect(request):
    district = tbl_district.objects.all()
    data=tbl_place.objects.all()
    if request.method=="POST":
        placeName=request.POST.get('txtname')
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        tbl_place.objects.create(place_name=placeName,district=dis)
        return redirect("Adminstrator:placeInsertSelect")
    else:
        return render(request,"Adminstrator/Place.html",{'data':data,"districtdata":district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("Adminstrator:placeInsertSelect")

def placeupdate(request,eid):
    district = tbl_district.objects.all()
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=request.POST.get("txtname")
        dis = tbl_district.objects.get(id=request.POST.get('sel_district'))
        editdata.district = dis
        editdata.save()
        return redirect("Adminstrator:placeInsertSelect")
    else:
        return render(request,"Adminstrator\Place.html",{"editdata":editdata,"districtdata":district})



def viewcomplaintlist(request):
    data=tbl_complaint.objects.all()
    return render(request,"Adminstrator/ViewComplaintList.html",{"data":data})       



def reply(request,cid):
    data=tbl_complaint.objects.get(id=cid)
    reply=tbl_reply.objects.all()
    if request.method=="POST":
        data.complaint_reply=request.POST.get("txtname")
        data.complaint_status=1
        data.save()
        return redirect("Adminstrator:reply",cid=cid)
    else:
        return render(request,"Adminstrator/Reply.html",{'data':reply})



def viewfeedback(request):
    data=tbl_feedback.objects.all()
    return render(request,"Adminstrator/ViewFeedback.html",{"data":data})       

