from django.http.response import HttpResponseForbidden
from accounts.models import Profile


class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                request.profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                request.profile = None 
        else:
            request.profile = None  

        response = self.get_response(request)
        return response
