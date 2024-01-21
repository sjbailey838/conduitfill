from django.urls import path
from .views import addCable, delete

app_name = "CableApp"

urlpatterns = [
    # path('/addcable', addCable,  name='cable-home'),
    path('addCable/', addCable, name = "add-cable"),
    path('delete/', delete, name = "delete"),
]
