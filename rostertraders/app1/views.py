from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from .models import Players, PlayerVals


def index(request):
	return render_to_response('app1/index.html', context_instance=RequestContext(request))



def player_vals(request):
	player_values = PlayerVals.objects.order_by('-value')
	player_values = player_values.select_related('pid').all()
	context     = {'player_list' : player_values}
	return render(request,'app1/portfolio.html',context)
