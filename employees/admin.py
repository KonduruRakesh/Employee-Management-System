from django.contrib import admin
from .models import Employee,Department,Leave
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','email','emp_id','dob','gender','designation','department','salary']
    ordering = ['id']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','description']
    ordering = ['id']

class LeaveAdmin(admin.ModelAdmin):
    list_display = ['employee','leave_type','from_date','to_date','description','applied_date','status']
    ordering = ['id']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Leave,LeaveAdmin)
