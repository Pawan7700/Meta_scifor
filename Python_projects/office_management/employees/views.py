from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Employee
import json

# Create your views here.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def employee_list(request):
    if request.method == "GET":
        employees = list(Employee.objects.values())  # List all employees
        return JsonResponse(employees, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        employee = Employee.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            position=data['position'],
            salary=data['salary']
        )
        return JsonResponse({'id': employee.id, 'first_name': employee.first_name, 'last_name': employee.last_name, 'email': employee.email, 'position': employee.position, 'salary': str(employee.salary)})

@csrf_exempt
@require_http_methods(["PUT", "DELETE"])
def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "PUT":
        data = json.loads(request.body)
        employee.first_name = data['first_name']
        employee.last_name = data['last_name']
        employee.email = data['email']
        employee.position = data['position']
        employee.salary = data['salary']
        employee.save()
        return JsonResponse({'id': employee.id, 'first_name': employee.first_name, 'last_name': employee.last_name, 'email': employee.email, 'position': employee.position, 'salary': str(employee.salary)})

    elif request.method == "DELETE":
        employee.delete()
        return JsonResponse({'message': 'Employee deleted successfully.'})


