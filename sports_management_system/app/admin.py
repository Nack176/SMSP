from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Custom Admin Site Configuration
admin.site.site_header = "Sports Management System"
admin.site.site_title = "SMS Admin"
admin.site.index_title = "Welcome to Sports Management System Admin"

# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','email','user_type','first_name','last_name','is_staff']
    list_filter = ['user_type','is_staff','is_active']
    search_fields = ['username','email','first_name','last_name']
    ordering = ['-date_joined']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('user_type','profile_pic')}),
    )

class StudentAdmin(admin.ModelAdmin):
    list_display = ['admin','gender','session_year_id']
    list_filter = ['gender','session_year_id']
    search_fields = ['admin__first_name','admin__last_name','admin__email']

class StaffAdmin(admin.ModelAdmin):
    list_display = ['admin','gender']
    list_filter = ['gender']
    search_fields = ['admin__first_name','admin__last_name','admin__email']

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name','sport','staff']
    list_filter = ['sport']
    search_fields = ['name']

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['tournament_id','attendance_data','session_year_id']
    list_filter = ['attendance_data','session_year_id']

admin.site.register(CustomUser,UserModel)
admin.site.register(Sport)
admin.site.register(Session_Year)
admin.site.register(Student,StudentAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(Tournament,TournamentAdmin)
admin.site.register(Staff_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Notification)
admin.site.register(Student_Feedback)
admin.site.register(Student_Leave)
admin.site.register(Attendance,AttendanceAdmin)
admin.site.register(Attendance_Report)
