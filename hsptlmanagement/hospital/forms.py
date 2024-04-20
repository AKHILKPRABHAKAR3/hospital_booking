from django import forms
from hospital.models import Booking

class Dateinput(forms.DateInput):
    input_type='date'

class BookingForm(forms.ModelForm):

    class Meta:
        model=Booking
        fields="__all__"
        widgets={
            'booking_date':Dateinput()
        }
        labels={
            'patient_name' : "Patient Name",
            'p_phone' : "Mobile No",
            'p_email' : "Email Address",
            'doc_name' : "Doctor Name",
            "booking_date" : "Booking Date",
        }


