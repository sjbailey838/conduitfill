from django.urls import path
from .views import addCable
app_name = "CableApp"

urlpatterns = [
    # path('/addcable', addCable,  name='cable-home'),
    path('addCable/', addCable, name = "add-cable"),

]
