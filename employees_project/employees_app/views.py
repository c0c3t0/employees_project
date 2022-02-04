from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from random import randint


# def home(request):
#     html = f'<h1>{request.method}: This is home.</h1>'
#     return HttpResponse(
#         html,
#         # content_type='text/plain',
#         # content_type='application/xml',
#         # content_type='application/json',
#         content_type=None,
#     )
from django.urls import reverse_lazy


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('department list'))
    print(reverse_lazy('department details', kwargs = {'id': 1},))
    print(reverse_lazy('not found'))
    context = {
        'number': randint(1, 1003),
        'numbers': [randint(1, 1003) for _ in range(4)],
    }
    return render(request, 'index.html', context)


def go_to_home(request):
    return redirect('department details', id=randint(1, 1024))


def not_found(request):
    return HttpResponseNotFound()
    # raise Http404()


def department_details(request, id):
    return HttpResponse(f'This is departments details {id}.')


def departments_list(request):
    return HttpResponse("This is list of departments.")
