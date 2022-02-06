from django import template

from employees_project.employees_app.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')
def departments_list():
    departments = Department.objects.all()

    return {
        'departments': departments,
    }
