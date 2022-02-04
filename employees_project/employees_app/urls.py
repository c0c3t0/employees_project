from django.urls import path

from employees_project.employees_app.views import home, department_details, departments_list, not_found, go_to_home

urlpatterns = [
    path('list/', departments_list, name='department list'),
    path('not_found/', not_found, name='not found'),
    path('<id>/', department_details, name='department details'),

]
