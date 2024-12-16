from django.contrib import admin
from hospital.models import Departments,Doctors,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','patient_name','p_phone','p_email','doc_name','booking_date')



# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
admin.site.register(Booking,BookingAdmin)
