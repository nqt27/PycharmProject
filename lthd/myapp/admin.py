from django.contrib import admin
from .models import Category, Courses

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date', 'category']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'created_date']

admin.site.register(Category)
admin.site.register(Courses, CourseAdmin)
# Register your models here.
