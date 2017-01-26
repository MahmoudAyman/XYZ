from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from courses.models import *
from django.shortcuts import render
from django.template import loader
from django.urls import reverse


# Create your views here.
def index (request):
	li = Course.objects.all()
	context={'courses':li}

	return render(request, "courses/courses.html", context)

def getCourseAbout (request, course_id):
	data =checkAuth()
	if(data[0]):
		name = Course.objects.get(pk=course_id).title
		return HttpResponse("Welcome to  "+name+" Course  "+data[1])
	else:
		return render(request, 'courses/form.html')

def getCourseVideos (request,id):
	pass

def getCourseAssig (request,id):
	pass

def getCourseMembers (request,id):
	pass

def checkAuth ():
	for i in Member.objects.all():
		if i.logged_in: return (True,i.first_name)
		else: return (False,)

def form(request):
	return render(request, 'courses/form.html')

def logIn(request):
	name = request.POST['username'].split(" ")[0]
	pwd = request.POST['password']
	context={}
	try:
		usr = Member.objects.get(first_name=name)
	except (KeyError, Member.DoesNotExist):
		context['errors']=True
		return render(request, "courses/form.html", context)
	else:
		if (usr.pwd == pwd):
			usr.logged_in=True
			usr.save()
			return HttpResponseRedirect(reverse('courses:index'))
		else: 
			return render(request, "courses/form.html", context)

def logOut(request):
	for i in Member.objects.all():
		i.logged_in=False
		i.save()
	return render(request, "courses/index.html")

def signUp(request):
	fname = request.POST['firstname']
	lname = request.POST['lastname']
	mail = request.POST['emailsignup']
	password = request.POST['passwordsignup']
	pwd2 = request.POST['passwordsignup_confirm']
	context={}

	if (password != pwd2):
		context['wrong']=True
		return render(request, "courses/form.html", context)
	else:
		mem = Member.objects.create(first_name=fname, last_name=lname, email=mail, pwd=password, logged_in=True)
		return HttpResponseRedirect(reverse('courses:index'))


	return HttpResponse("signup")


