from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['Title',"Price","Duration"]
    

admin.site.register(Course,CourseAdmin)
