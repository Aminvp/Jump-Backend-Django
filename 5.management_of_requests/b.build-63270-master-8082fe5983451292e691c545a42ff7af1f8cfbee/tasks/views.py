from django.http import HttpResponse
from .models import Task


def list_create_tasks(request):
    if request.method == 'GET':
        query = Task.objects.order_by('name').values_list('name', flat=True)
        return HttpResponse('<br>'.join(map(str, query)))


def count_tasks(request):
    if request.method == 'GET':
        query = Task.objects.count()
        return HttpResponse(f"You have '{query}' tasks to do")
