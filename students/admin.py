from django.contrib import admin
from .models import Student, School


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'grade',
        'school',
        'registration_date',
    ]

    search_fields = [
        'first_name',
        'last_name',
        'email',
    ]

    list_filter = [
        'grade',
        'school',
    ]


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'address',
        'user',
    ]

    search_fields = [
        'name',
        'address',
    ]