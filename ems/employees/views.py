from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Department, Leave


def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        emp_id = request.POST['emp_id']
        dob = request.POST['dob']
        gender = request.POST['gender']
        designation = request.POST['designation']
        department_id = request.POST['department']
        salary = request.POST['salary']
        department = Department.objects.get(id=department_id)
        employee = Employee(
            name=name,
            email=email,
            emp_id=emp_id,
            dob=dob,
            gender=gender,
            designation=designation,
            department=department,
            salary=salary
        )
        employee.save()
        return redirect('employee_list')
    
    departments = Department.objects.all()
    return render(request, 'add_employee.html', {'departments': departments})


def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.emp_id = request.POST['emp_id']
        employee.dob = request.POST['dob']
        employee.gender = request.POST['gender']
        employee.designation = request.POST['designation']
        department_id = request.POST['department']
        employee.department = Department.objects.get(id=department_id)
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')
    
    departments = Department.objects.all()
    context = {
        'employee': employee,
        'departments': departments,
    }
    return render(request, 'edit_employee.html', context)
   

def view_employee(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    return render(request, 'view_employee.html', {'employee': employee})

def leave_history(request, emp_id):
    employee = get_object_or_404(Employee, emp_id=emp_id)
    leaves = Leave.objects.filter(employee=employee)
    return render(request, 'leave_history.html', {'leaves': leaves})

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']

        department = Department(
            name=name,
            description=description
        )
        department.save()
        return redirect('department_list')
 
    return render(request, 'add_department.html')


def edit_department(request,id):
    department = get_object_or_404(Department, id=id)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.description = request.POST['description']
        department.save()
        return redirect('department_list')
    context = {
        'department': department
    }
    return render(request, 'edit_department.html', context)


def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    department.delete()
    return redirect('department_list')