from django.contrib import admin
from .models import Sbook,Addser,Book_status,Booking_paid

# Register your models here.
admin.site.register(Sbook)
admin.site.register(Addser)
admin.site.register(Book_status)
admin.site.register(Booking_paid)
