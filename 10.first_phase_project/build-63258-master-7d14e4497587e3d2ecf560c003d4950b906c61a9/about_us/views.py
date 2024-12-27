from accounts.models import User
from django.shortcuts import render


def about_us(request):
    # View for about-us page
    users = User.objects.all()
    return render(request, 'about_us.html', {'users': users})
