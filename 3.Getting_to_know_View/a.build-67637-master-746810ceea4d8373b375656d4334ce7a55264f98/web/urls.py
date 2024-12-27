from django.urls import path

from .views import *

urlpatterns = [
    path("sad/<str:name>/", rangesh),
    path("happy/<str:name>/<int:times>/", khosh_barkhord)
]
