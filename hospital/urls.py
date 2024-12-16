
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from hospital import views

urlpatterns = [
    path("home/",views.Home.as_view(),name="home"),
    path("department/",views.DepartmentView.as_view(),name="dept"),
    path("doctors/",views.DoctorsView.as_view(),name="doctors"),
    path("booking/",views.Bookingview.as_view(),name="booking"),
    path("contact_us/",views.ContactUs.as_view(),name="contact_us"),
    path("about/",views.AboutView.as_view(),name="about"),
    path("patients/",views.Patientsview.as_view(),name="patients"),
    path("patientsdelete/<int:id>",views.PatientDeleteView.as_view(),name="patientdelete"),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)