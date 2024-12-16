from django.shortcuts import render,redirect
from django.views import View
from hospital.models import Departments,Doctors,Booking
from hospital.forms import BookingForm

class Home(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    # Create your views here.

class DepartmentView(View):
    def get(self,request,*args,**kwargs):
        data=Departments.objects.all()
        return render(request,"dept.html",{"form":data})
class DoctorsView(View):
    def get(self,request,*args,**kwargs):
        data=Doctors.objects.all()
        return render(request,"doctors.html",{"data":data})
    
class Bookingview(View):
    def get(self,request,*args,**kwargs):
        form=BookingForm()
        return render(request,"booking.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            form=BookingForm()
            print("booking successfull")
            return render(request,"confirmation.html")
        else:
            print("form is not valid")
        return render(request,"booking.html",{"form":form})
    
class ContactUs(View):
    def get(self,request,*args,**kwargs):
        return render(request,"contact_us.html")
    
class AboutView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"about.html")
    
class Patientsview(View):
    def get(self,request,*args,**kwargs):
        data=Booking.objects.all()
        return render(request,"patients.html",{"data":data})
    
class PatientDeleteView(View):
    def get(self,request,*args,**kwargs):
        k=kwargs.get("id")
        data=Booking.objects.get(id=k).delete()
        return redirect("patients")

