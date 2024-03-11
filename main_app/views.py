from django.db import models
from django.views.generic import ListView

from main_app.models import Employee


class TopManagementListView(ListView):
    model = Employee
    template_name = 'index.html'
    context_object_name = 'top_management'

    def get_queryset(self):
        return Employee.objects.filter(boss=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for manager in context['object_list']:
            manager.subordinates = manager.subordinates
        return context


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employees'
    ordering = 'last_name'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                models.Q(first_name__icontains=search_query) |
                models.Q(last_name__icontains=search_query) |
                models.Q(middle_name__icontains=search_query) |
                models.Q(position__icontains=search_query) |
                models.Q(email__icontains=search_query)
            )
        return queryset
