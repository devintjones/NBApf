from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from social_auth import __version__ as version


from .models import Players, PlayerVals, Pf, PfValue, AuthUser


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def contact(request):
	return render_to_response('contact.html', context_instance=RequestContext(request))

def home(request):
	return HttpResponseRedirect('/players')

@login_required(login_url='/login/facebook')
def player_vals(request):
	
	# get list of players and their valuations
	player_values = PlayerVals.objects.order_by('-value')
	player_values = player_values.select_related('pid').all()
	
	# get user portfolio contents
	this_user = request.user
	pf_contents = Pf.objects.filter(user=this_user.id).select_related('pid').all()

	# get user value or initialize a new one
	user_pf,created   = PfValue.objects.get_or_create(user=this_user.id,
						defaults={'user': AuthUser.objects.get(id=this_user.id),
							'cash'  : 10000})


	print user_pf
	context   = {'player_list' : player_values,
			'pf_contents'  : pf_contents,
			'user_pf' : user_pf}
	return render(request,'portfolio.html',context)


# update portfolio holdings and cash value
def sell_shares(request):
	this_user = request.user
	success=True
	for pid,share_num in request.POST.iteritems():
		if pid != 'csrfmiddlewaretoken' and share_num !='':
			share_num = int(share_num)	
			# update user portfolio share values
			entry        = Pf.objects.get(user=this_user.id,pid=pid)
			if entry.shares < share_num:
				messages.error(request,"Sorry, you don't own enough shares to complete that trade!")
				success=False
				break
			entry.shares -= share_num
			entry.save()
			
			# update cash value
			player_share_price = PlayerVals.objects.get(pid=pid).value
			cash_add           = share_num * player_share_price
			user_pf            = PfValue.objects.get(user=this_user.id)
			user_pf.cash       += cash_add
			user_pf.save()

	if success: messages.success(request,"Trade excuted successfuly!")

	return HttpResponseRedirect('/players')


# update portfolio holdings and cash value
def buy_shares(request):
	this_user = request.user
	success=True
	for pid,share_num in request.POST.iteritems():
		if pid != 'csrfmiddlewaretoken' and share_num !='':
			
			# update cash value
			player_share_price = PlayerVals.objects.get(pid=pid).value
			less_cash          = int(share_num) * player_share_price
			user_pf            = PfValue.objects.get(user=this_user.id)
			if user_pf.cash < less_cash:
				messages.error(request,"Sorry, you don't have enough cash to complete that trade!")
				success=False
				break

			user_pf.cash       -= less_cash
			user_pf.save()
			
			# update or create entry in portfolio (with more logic than django update_or_create() )
			try:
				entry        = Pf.objects.get(user=this_user.id,pid=pid)
				entry.shares += int(share_num)
				entry.save()
			except Pf.DoesNotExist:
				# must use classes from models.py when creating db objects
				user         = AuthUser.objects.get(id=this_user.id)
				player       = Players.objects.get(pid=pid)
				entry        = Pf.objects.create(user=user,pid=player,
								id='{}{}'.format(pid,share_num),shares=int(share_num))
				entry.save()

	if success: messages.success(request,"Trade excuted successfuly!")

	return HttpResponseRedirect('/players')


def logout(request):
	auth_logout(request)
	return HttpResponseRedirect('/')

