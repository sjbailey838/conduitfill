from django.urls import path
from .views import addCable, deleteCableRun, deleteConduitRun,deleteConduit, deleteCable

app_name = "CableApp"

urlpatterns = [
    # path('/addcable', addCable,  name='cable-home'),
    path('addCable/', addCable, name='add-cable'),
    path('deleteConduitRun/<id>', deleteConduitRun, name='deleteConduitRun'),
    path('deleteCableRun/<id>', deleteCableRun, name='deleteCableRun'),
    path('deleteConduit/<id>', deleteConduit, name='deleteConduit'),
    path('deleteCable/<id>', deleteCable, name='deleteCable'),

]
