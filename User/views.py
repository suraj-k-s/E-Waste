from django.shortcuts import render,redirect
from Guest.models import *
from User.models import *
from django.conf import settings
import os
from ultralytics import YOLO

import torch


def Detect(request):

  if request.method == 'POST' and request.FILES['image']:
    try:
      image = request.FILES['image']
      temp_image_path = os.path.join(settings.MEDIA_ROOT, 'temp_image.jpg')
      with open(temp_image_path, 'wb+') as destination:
        for chunk in image.chunks():
          destination.write(chunk)
      print('-'*40)
      detected_e_waste = perform_detection(temp_image_path)
      context = {'detected_e_waste': detected_e_waste}
      return render(request, 'User/Detect.html', context)
    except Exception as e:
      error_message = f"An error occurred: {str(e)}"
      return render(request, 'User/Detect.html', {'error_message': error_message})
  return render(request, 'User/Detect.html')

def perform_detection(image_path, saved_model_path="yolov8s.pt"):
    yolo = YOLO(saved_model_path)
    results = yolo(image_path)

    detected_e_waste = []

    for result in results:
        boxes = result.boxes

        tensor_list = boxes.cls.tolist()

        for item in tensor_list:
            detected_e_waste.append(result.names[int(item)])

    return detected_e_waste


def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_user.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")


def companylist(request):
    data=tbl_company.objects.all()
    return render(request,"User/CompanyList.html",{'data':data})


def request(request,did):
    requests = tbl_request.objects.all()
    cmpny=tbl_company.objects.get(id=did)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        requestdate=request.POST.get('txtdate')
        requestamount=request.POST.get('txtamount')
        requeststatus=request.POST.get('txtstatus')
        tbl_request.objects.create(request_date=requestdate,request_amount=requestamount,user=userdata,company=cmpny)
        return redirect("User:companylist")
    else:
        return render(request,"User/Request.html",{"data":requests})



def viewrequest(request):
    prodata=tbl_user.objects.get(id=request.session["uid"])
    data=tbl_request.objects.filter(user=prodata)
    return render(request,"User/ViewRequest.html",{"data":data})
    
def complaint(request):
    complaint = tbl_complaint.objects.all()
    userdata=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        complainttitle=request.POST.get('txttitle')
        complaintdetails=request.POST.get('txtdetails')
        tbl_complaint.objects.create(complaint_title=complainttitle,complaint_details=complaintdetails,user=userdata)
        return redirect("User:complaint")
    else:
        return render(request,"User/Complaint.html",{"data":complaint})


def feedback(request):
    feedback = tbl_feedback.objects.all()
    if request.method=="POST":
        feedbacktitle=request.POST.get('txttitle')
        feedbackdetails=request.POST.get('txtdetails')
        tbl_feedback.objects.create(feedback_title=feedbacktitle,feedback_details=feedbackdetails)
        return redirect("User:feedback")
    else:
        return render(request,"User/Feedback.html",{"data":feedback})

 