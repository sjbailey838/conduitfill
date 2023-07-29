from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cable, Conduit, CableRun, ConduitRun
from .forms import CableForm, ConduitForm,ConduitRunForm,CableRunForm

# Create your views here.
@login_required
def addCable(request):
    form = CableForm()
    form1 = ConduitForm()
    form2 = CableRunForm()
    form3 = ConduitRunForm()
    conduits = Conduit.objects.all()
    cables = Cable.objects.all()
    conduitruns = ConduitRun.objects.all()
    cableruns = CableRun.objects.all()
    print(conduitruns,"this is the cables assigned to this conduit")
    print(cableruns,"is the cable runs")
    cablelist = []
    # for i in range(len((conduitruns))):
    #     print(conduitruns[i].conduittag,conduitruns[i].cable.all())
    #     cablelist.append(conduitruns[i].cable.all()) 
    # print(cablelist, "is your list of cables")
    # cablequery = conduitruns[0].cable.all()
    # print(conduitruns)
    # print(cablequery)
    if request.method == 'POST':
        # print(request.POST)
        if 'addcable' in request.POST:
            form = CableForm(request.POST)
            if form.is_valid():
                form.save()
        elif 'addconduit' in request.POST:
            form1 = ConduitForm(request.POST)
            if form1.is_valid():
                form1.save()
        elif 'projectcable' in request.POST:
            form2 = CableRunForm(request.POST)
            if form2.is_valid():
                form2.save()
        elif 'projectconduit' in request.POST:
            form3 = ConduitRunForm(request.POST)
            if form3.is_valid():
                form3.save()
    context = {'form':form,'form1':form1,'conduits':conduits, 'cables':cables,
            'conduitruns':conduitruns,'cableruns':cableruns,'form2':form2,'form3':form3, 'cablelist':cablelist
               }
    return render(request, 'users/addcable.html',context)
    