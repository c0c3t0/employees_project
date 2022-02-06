from django.urls import path

from employees_project.templates_examples.views import index

urlpatterns = (
    path('', index, name='templates index'),
)