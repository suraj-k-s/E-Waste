from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from Company.models import *
from Adminstrator.models import *


from django.conf import settings
import os
from ultralytics import YOLO

def Detect(request):
  if request.method == 'POST' and request.FILES['image']:
    try:
      image = request.FILES['image']
      temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
      with open(temp_image_path, 'wb+') as destination:
        for chunk in image.chunks():
          destination.write(chunk)
      detected_e_waste = perform_detection(temp_image_path)
      context = {'detected_e_waste': detected_e_waste}
      return render(request, 'User/Detect.html', context)
    except Exception as e:
      error_message = f"An error occurred: {str(e)}"
      return render(request, 'Company/Detect.html', {'error_message': error_message})
  return render(request, 'Company/Detect.html')

def perform_detection(image_path, saved_model_path="yolov8s.pt"):
    yolo = YOLO(saved_model_path)
    results = yolo(image_path)
    detected_objects = []
    
    for result in results:
        boxes = result.boxes
        tensor_list = boxes.cls.tolist()
        
        for item in tensor_list:
            name = result.names[int(item)]
            found = False
            for obj in detected_objects:
                if obj['name'] == name:
                    obj['count'] += 1
                    found = True
                    break
            if not found:
                detected_objects.append({'name': name, 'count': 1})
    return detected_objects




def homepage(request):
    return render(request,"Company/HomePage.html")

def my_pro(request):
    data=tbl_company.objects.get(id=request.session["cid"])
    return render(request,"Company/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_company.objects.get(id=request.session["cid"])
    if request.method=="POST":
        prodata.cmp_name=request.POST.get('txtname')
        prodata.cmp_contact=request.POST.get('txtcon')
        prodata.cmp_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Company/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Company/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_company.objects.filter(id=request.session["cid"],cmp_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                companydata=tbl_company.objects.get(id=request.session["cid"],cmp_password=request.POST.get('txtcurpass'))
                companydata.cmp_password=request.POST.get('txtnewpass')
                companydata.save()
                return render(request,"Company/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Company/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Company/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"Company/ChangePassword.html")



def requestlist(request):
    requestdata = tbl_request.objects.filter(request_status=0)
    return render(request,"Company/RequestList.html",{"requestdata":requestdata})

def acceptrequest(request,aid):
    arequest = tbl_request.objects.get(id=aid)
    arequest.request_status = 1
    arequest.save()
    return redirect("Company:homepage")

def rejectrequest(request,rid):
    rrequest = tbl_request.objects.get(id=rid)
    rrequest.request_status = 2
    rrequest.save()
    return redirect("Company:homepage")

def requestListAccepted(request):
    requestdata = tbl_request.objects.filter(request_status=1)
    return render(request,"Company/RequestListAccepted.html",{"requestdata":requestdata})

def requestListRejected(request):
    requestdata = tbl_request.objects.filter(request_status=2)
    return render(request,"Company/RequestListRejected.html",{"requestdata":requestdata})


def waste(request,did):
    category = tbl_Category.objects.all()
    requestData = tbl_request.objects.get(id=did)
    waste =tbl_waste.objects.all()
    if request.method=="POST":
        categorys = tbl_Category.objects.get(id=request.POST.get('sel_Category'))
        tbl_waste.objects.create(waste_quantity=request.POST.get("txtquantity"),category=categorys,request=requestData)
        return render(request,"Company/Waste.html",{'data':waste,"category":category})
    else:
        return render(request,"Company/Waste.html",{'data':waste,"category":category})

def logout(request):
    del request.session["cid"]
    return redirect("Guest:Login")


