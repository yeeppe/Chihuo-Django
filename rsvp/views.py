# Create your views here.
from forms import RSVPCreateEventFormStep1
from forms import RSVPCreateEventFormStep2
from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from rsvp.models import ChihuoEvent


def create_event_step1(request):
	form = RSVPCreateEventFormStep1()
	return render_to_response('rsvp/create-event.html', 
			{
				'form' : form ,
				'step' : 1,
			},
			context_instance=RequestContext(request)
	)
	
	
def create_event_step2(request):
	if request.method == 'POST':
		form = RSVPCreateEventFormStep1(request.POST) 	# get submitted form
		if form.is_valid():
			title = form.cleaned_data['title']
			newform = RSVPCreateEventFormStep2()		# create next form
		return render_to_response('rsvp/create-event.html',
			 	{
					'form' : newform,
					'step' : 2,
					'data': title,
				},
				context_instance=RequestContext(request)
		)

	else:
		newform = RSVPCreateEventFormStep1()
		return render_to_response('rsvp/create-event.html', 
				{
					'form' : newform ,
					'step' : 1,
				},
				context_instance=RequestContext(request)
		)

def create_event_step3(request):
	if request.method == 'POST':
		form = RSVPCreateEventFormStep2(request.POST) 	# get submitted form
		if form.is_valid():
			title = form.cleaned_data['title']
			newform = RSVPCreateEventFormStep3()		# create next form
			return render_to_response('rsvp/create-event.html',
			 	{
					'form' : newform,
					'step' : 3,
					'data': title,
				},
				context_instance=RequestContext(request)
			)

		else:
			newform = RSVPCreateEventFormStep1()
			return render_to_response('rsvp/create-event.html', 
				{
					'form' : newform ,
					'step' : 1,
				},
				context_instance=RequestContext(request)
			)

def create_event_step_final(request):
	if request.method == 'POST':
		form = RSVPCreateEventFormStep3(request.POST)
		if form.is_valid():
			# get data
			# create new chihuo event
			return render_to_response('rsvp/create-event-successful.html',
				{
					'data'	: 'successful',
				},
				context_instance=RequestContext(request)
			)
	else:
		newform = RSVPCreateEventFormStep1()
		return render_to_response('rsvp/create-event.html', 
			{
				'form' : newform ,
				'step' : 1,
			},
			context_instance=RequestContext(request)
		)	


