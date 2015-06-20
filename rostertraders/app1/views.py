from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from social_auth import __version__ as version


from .models import Players, PlayerVals, Pf, PfValue


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))


@login_required(login_url='/login/facebook')
def player_vals(request):
	
	# get list of players and their valuations
	player_values = PlayerVals.objects.order_by('-value')
	player_values = player_values.select_related('pid').all()
	
	# get user portfolio contents
	this_user = request.user
	portfolio = Pf.objects.filter(user=this_user.id).select_related('pid').all()

	# get user value
	user_value = PfValue.objects.filter(user=0)[0]

	context     = {'player_list' : player_values,
			'portfolio'  : portfolio,
			'user_value' : user_value}
	return render(request,'portfolio.html',context)

def sell_shares(request):
	print(request.POST.keys())
	for pid,share_num in request.POST.iteritems():
		if pid != 'csrfmiddlewaretoken' and share_num !='':
			entry = Pf.objects.get(user=request.user.id,pid=pid)
			entry.shares = entry.shares - int(share_num)
			entry.save()

	return HttpResponseRedirect('/players')



def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')

