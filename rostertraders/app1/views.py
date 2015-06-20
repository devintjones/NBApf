from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from social_auth import __version__ as version


from .models import Players, PlayerVals, Pf


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))


@login_required(login_url='/login/facebook')
def player_vals(request):
	
	# get list of players and their valuations
	player_values = PlayerVals.objects.order_by('-value')
	player_values = player_values.select_related('pid').all()
	
	# get user portfolio
	this_user = request.user
	#portfolio = Pf.objects.filter(uid=0).select_related('pid')
	portfolio = Pf.objects.filter(uid=this_user.id).select_related('pid').all()
	
	context     = {'player_list' : player_values,
			'portfolio'  : portfolio}
	return render(request,'portfolio.html',context)

def trade(request):

	# execute sql query for post request

	return HttpResponseRedirect('/players')



def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')

