from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import ListView

from .models import Employee

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

