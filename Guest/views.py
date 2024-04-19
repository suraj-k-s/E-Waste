from django.shortcuts import render,redirect
from Adminstrator.models import *
from Guest.models import *

# Create your views here.
def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district=dis)
    return render(request,"Guest/AjaxPlace.html",{"placedata":place})
    


def userRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_user.objects.create(user_name=request.POST.get("txtname"),user_gender=request.POST.get("gender"),user_contact=request.POST.get("txtcontact"),user_email=request.POST.get("txtemail"),user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),user_password=request.POST.get("txtpwd"),place=place)
        return redirect("Guest:userRegistration")
    else:
        return render(request,"Guest/NewUser.html",{"districtdata":district})


def cmpRegistration(request):
    district = tbl_district.objects.all()
    if request.method=="POST":
        place = tbl_place.objects.get(id=request.POST.get('sel_place'))
        tbl_company.objects.create(cmp_name=request.POST.get("txtname"),cmp_contact=request.POST.get("txtcontact"),cmp_email=request.POST.get("txtemail"),cmp_password=request.POST.get("txtpwd"),cmp_photo=request.FILES.get("fileImage"),cmp_proof=request.FILES.get("fileProof"),place=place)
        return redirect("Guest:cmpRegistration")
    else:
        return render(request,"Guest/Company.html",{"districtdata":district})




def Login(request):
    if request.method == "POST":
        usercount = tbl_user.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        companycount = tbl_company.objects.filter(cmp_email=request.POST.get("txt_email"),cmp_password=request.POST.get("txt_password")).count()
        adminregistrationcount = tbl_adminregistration.objects.filter(AdminRegistration_email=request.POST.get("txt_email"),AdminRegistration_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_user.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:homepage")
        elif companycount > 0:
            cmp = tbl_company.objects.get(cmp_email=request.POST.get("txt_email"),cmp_password=request.POST.get("txt_password"))
            request.session["cid"] = cmp.id
            request.session["cname"] = cmp.cmp_name
            return redirect("Company:homepage")
        elif adminregistrationcount > 0:
            AdminRegistration = tbl_adminregistration.objects.get(AdminRegistration_email=request.POST.get("txt_email"),AdminRegistration_password=request.POST.get("txt_password"))
            request.session["aid"] = AdminRegistration.id
            request.session["aname"] = AdminRegistration.AdminRegistration_name
            return redirect("Adminstrator:LoadingHomePage")
            
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")



def index(request):
    return render(request,"Guest/index.html")