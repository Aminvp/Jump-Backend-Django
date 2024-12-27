from django.http import HttpResponse


def rangesh(request, name):
    response = f'Nobody likes you, {name}!'
    return HttpResponse(response)

def khosh_barkhord(request, name , times):
    response = ''
    for time in range(times):
        response += f'You are great, {name} :)<br>' 
    return HttpResponse(response)
