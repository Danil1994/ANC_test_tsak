from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.http import JsonResponse

from main_app.models import Employee


def index(request):
    return render(request, 'index.html')


def get_subordinates(request, pk):
    employee = Employee.objects.get(pk=pk)
    subordinates = employee.subordinates

    return render(
        request,
        'main_app/subordinates.html',
        context={'subordinates': subordinates}
    )


class TopManagementListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'main_app/top_management_list.html'
    context_object_name = 'top_management'

    def get_queryset(self):
        return Employee.objects.filter(boss=None)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for manager in context['object_list']:
            manager.subordinates = manager.subordinates
        return context


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'main_app/employee_list.html'
    context_object_name = 'employees'
    ordering = 'last_name'
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()

        order_by = self.request.GET.get('order_by')
        if order_by:
            queryset = queryset.order_by(order_by)
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(middle_name__icontains=search_query) |
                Q(position__icontains=search_query) |
                Q(email__icontains=search_query)
            )

        return queryset


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    fields = ['first_name', 'last_name', 'middle_name', 'position', 'hire_date', 'email', 'boss']
    success_url = reverse_lazy('employee_list')

    def form_valid(self, form):
        # Проверяем, была ли указана дата приема на работу
        if not form.cleaned_data['hire_date']:
            # Если не была указана, устанавливаем сегодняшнюю дату
            form.instance.hire_date = now().date()
        return super().form_valid(form)


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'middle_name', 'position', 'hire_date', 'email', 'boss']
    success_url = reverse_lazy('employee_list')
    template_name_suffix = "_update_form"


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy("employee_list")
