from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cable, Conduit, CableRun, ConduitRun
from .forms import CableForm, ConduitForm,ConduitRunForm,CableRunForm
from django.urls import reverse

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
    # print(conduitruns,"this is the cables assigned to this conduit")
    # print(cableruns,"is the cable runs")
    # conduitruns

        
        
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

    for conduit in conduits:
        conduit.Area = Conduit.calculate_area(conduit.InnerDimension)
        conduit.save()

    for conduitrun in conduitruns:
        sumlist = []
        cablelist = conduitrun.cable.all()
        for cable in cablelist:
            result = 3.14*(cable.cable.OuterDimension/2)**2
            sumlist.append(result)
        totalcablearea = sum(sumlist)
        conduitrun.fill = (totalcablearea / conduitrun.conduit.Area)

    context = {'form':form,'form1':form1,'conduits':conduits, 'cables':cables,
            'conduitruns':conduitruns,'cableruns':cableruns,'form2':form2,'form3':form3, 
               }
    return render(request, 'addcable.html',context)


@login_required
def deleteConduitRun(request, id):
    try:
        rtd = ConduitRun.objects.get(pk=id)
        rtd.delete()
        return redirect(reverse('CableApp:add-cable'))
    except ConduitRun.DoesNotExist:
        print("ohno")
        return redirect(reverse('CableApp:add-cable'))

@login_required
def deleteCableRun(request, id):
    try:
        rtd = CableRun.objects.get(pk=id)
        rtd.delete()
        return redirect(reverse('CableApp:add-cable'))
        # context = {'id':id,}
    except CableRun.DoesNotExist:
        print("ohno")
        return redirect(reverse('CableApp:add-cable'))

@login_required
def deleteConduit(request, id):
    try:
        rtd = Conduit.objects.get(pk=id)
        rtd.delete()
        return redirect(reverse('CableApp:add-cable'))
        # context = {'id':id,}
    except Conduit.DoesNotExist:
        print("ohno")
        return redirect(reverse('CableApp:add-cable'))
    
@login_required
def deleteCable(request, id):
    try:
        rtd = Cable.objects.get(pk=id)
        rtd.delete()
        return redirect(reverse('CableApp:add-cable'))
        # context = {'id':id,}
    except Cable.DoesNotExist:
        print("ohno")
        return redirect(reverse('CableApp:add-cable'))

