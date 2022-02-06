from django.http import HttpResponse
from django.shortcuts import render

from employees_project.employees_app.models import Employee, Department


def index(request):
    context = {
        'num_1': 123,
        'num_2': 321,
        'num_3': 200,
        'numbers': [123, 321, 200],
        'title': 'empLOyees liSt',
        'employees': Employee.objects.order_by('first_name', 'department'),
        'departments': [d.name for d in Department.objects.all()],
    }
    return render(request, 'template_examples/index.html', context)
