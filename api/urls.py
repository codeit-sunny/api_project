from django.urls import path
from .views import get_employees, create_employees,update_employee, delete_employee

urlpatterns = [
path('employees/',get_employees),
path('create/',create_employees),
path('update/<int:pk>/', update_employee),
path('delete/<int:pk>/', delete_employee),
]