from django.contrib import admin
from .models import Login
from .models import Add
class FciAdmin(admin.ModelAdmin):
    list_display=['Name','Id','Gpa','Level','Department','Status']
    list_display_links=['Name','Id']
    list_editable=['Gpa','Level','Department','Status']
    search_fields=['Name']
    list_filter=['Status','Department']
admin.site.register(Login)
admin.site.register(Add,FciAdmin)
admin.site.site_header='Student Affiars'
admin.site.site_title='Student Affiars'

# Register your models here.
