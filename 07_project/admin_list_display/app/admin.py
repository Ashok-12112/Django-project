from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'city')
    list_filter = ('city','age')
    search_fields = ('age',)
    ordering = ('age',)