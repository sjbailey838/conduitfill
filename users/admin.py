from django.contrib import admin
from .models import Profile,Cable,CableRun,Conduit, ConduitRun
#
# InnerDimension,OuterDimension,Conduit JacketRating,Conductors,CableSize, 
admin.site.register(Profile)
admin.site.register(Cable)
admin.site.register(CableRun)
admin.site.register(Conduit)
admin.site.register(ConduitRun)
# admin.site.register(CableSize)
# admin.site.register(JacketRating)
# admin.site.register(Conductors)
# admin.site.register(InnerDimension)
# admin.site.register(OuterDimension)
# admin.site.register(Conduit)
