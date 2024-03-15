from django.contrib import admin
from website.models import BasicInformationModel

# Register your models here.
class BasicInformationAdmin(admin.ModelAdmin):
    list_display =['id','age']


admin.site.register( BasicInformationModel,BasicInformationAdmin)
