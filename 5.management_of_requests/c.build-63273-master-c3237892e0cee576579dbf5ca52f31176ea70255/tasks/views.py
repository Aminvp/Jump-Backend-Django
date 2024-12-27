from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import HttpResponse

@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        name = request.POST.get('task')  
        if name:  
            Task.objects.create(name=name)  
            return HttpResponse(f"Task Created: '{name}'") 
        return HttpResponse("No task provided")  