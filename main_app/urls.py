from django.urls import path
from . import views

urlpatterns = [
    path('', views.TopManagementListView.as_view(), name='index'),
    path('/employees/', views.EmployeeListView.as_view(), name='employee_list'),
]
