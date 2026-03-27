from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employees
from .serializers import EmployeesSerializer


@api_view(['GET'])
def get_employees(request):
    employees = Employees.objects.all()
    serializer = EmployeesSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_employees(request):
    serializer = EmployeesSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def update_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    serializer = EmployeesSerializer(employee, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_employee(request, pk):
    employee = Employees.objects.get(id=pk)
    employee.delete()
    return Response("Deleted Successfully")

