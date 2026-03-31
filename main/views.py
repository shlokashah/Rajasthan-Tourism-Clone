from django.shortcuts import render
from .models import *
from django.db.models import *
# Create your views here.

def home(request):
	top_places = Place.objects.annotate(avg_rate = Avg('rating')).order_by('-avg_rate')[:4]
	return render(request,'base.html',{'top_places': top_places.all() })