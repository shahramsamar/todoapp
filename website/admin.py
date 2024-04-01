from django.contrib import admin
from website.models import BasicInformationModel, SkillModel

# Register your models here.
class BasicInformationAdmin(admin.ModelAdmin):
    list_display =['email','age']

class SkillAdmin(admin.ModelAdmin):
    list_display =['title','level']
    
    
admin.site.register( BasicInformationModel, BasicInformationAdmin)
admin.site.register(SkillModel, SkillAdmin)
