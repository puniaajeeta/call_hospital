from django.contrib import admin
from medicine_app.models import City,Hospitals

# Register your models here.
# class City(admin.ModelAdmin):
#     list_display = ['city_name']

class CityAdmin(admin.ModelAdmin):
    list_display = ["city_name"]

class hostpitalAdmin(admin.ModelAdmin):
    list_display = ["city_name","city_hospital","hospital_number"]    


admin.site.register(City,CityAdmin)
admin.site.register(Hospitals,hostpitalAdmin)
