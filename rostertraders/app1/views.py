from django.shortcuts import render
from django.http import HttpResponse

from .models import Players, PlayerVals

def index(request):
	return HttpResponse("Hello, world!")

def player_vals(request):
	player_values = PlayerVals.objects.order_by('-value')
	player_values = player_values.select_related('pid').all()
	context     = {'player_list' : player_values}
	return render(request,'app1/index.html',context)
