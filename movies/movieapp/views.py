from django.shortcuts import render, get_object_or_404
from .models import actionTracks,recordLabels

# Create your views here.
def index(request):
    return render(request, 'tracks/index.html')
def gettracks(request):
    tracks_list=actionTracks.objects.all()
    return render(request,'tracks/action.html', {'tracks_list' : tracks_list} )