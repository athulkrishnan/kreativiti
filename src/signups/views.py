from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import messages
import sendgrid

# Create your views here.
from .forms import SignUpForm


def home(request):
	return render_to_response("base.html", RequestContext(request))


def thankyou(request):
	return render_to_response("thankyou.html",
					locals(),
					context_instance=RequestContext(request))

def portfolio(request):
	return render_to_response("portfolio.html", RequestContext(request))

def enquire(request):

	form = SignUpForm(request.POST or None)
	
	if form.is_valid():
#Sendgrid start
		sg = sendgrid.SendGridClient('athulkrishnan', 'W@lkinglif3+')
		message = sendgrid.Mail()
		message.add_to('Athul Krishnan <atk007@gmail.com>')
		message.add_to('Pratheesh Prakash <royal.mexian@gmail.com>')
		message.add_to('Yassin Muhammed <yassin.muhammed@gmail.com>')
		message.add_to('Sajith Nambidi <sajith.nambidi@gmail.com>')		
		message.set_subject('Kreativiti Images: Enquiry')
		userid = 'some dude.'
		message.set_text("Yo!\n \nWe have a new quote request from " + userid + "\nPlease logon to www.kreativiti.in/admin/ to check details.\n" + " \nRegards, \nAthul Krishnan \nTech Guy @ Kreativiti")
		message.set_from('Kreativiti Images <shoot@kreativiti.in>')
		status, msg = sg.send(message)
#Sendrgrid end

		save_it = form.save(commit=False)
		save_it.save()
		messages.success(request, 'We will be in touch')
		return HttpResponseRedirect('/thank-you/')

	return render_to_response("signup.html",
					locals(),
					context_instance=RequestContext(request))
