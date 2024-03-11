from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('top_management/', views.TopManagementListView.as_view(), name='top_management'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
]
