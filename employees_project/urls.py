from django.contrib import admin
from django.urls import path, include

from employees_project.employees_app.views import home, go_to_home

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('go_to_home/', go_to_home, name='go to home'),
    path('departments/', include('employees_project.employees_app.urls')),
    path('templates/', include('employees_project.templates_examples.urls')),
)
