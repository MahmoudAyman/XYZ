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
	data =checkAuth(request)
	if(data!=False):
		name = Course.objects.get(pk=course_id).title
		Posts=Course.objects.get(pk=course_id).post_set.all()
		Notis=Course.objects.get(pk=course_id).notification_set.all()
		coms=Course.objects.get(pk=course_id).comment_set.all()
		context={'post':Posts, 'not':Notis,'com':coms,'cid':course_id}
		return render(request, "courses/about.html",context)
	else:
		return render(request, 'courses/form.html')

def getCourseVideos (request,id):
	pass

def getCourseAssig (request,id):
	pass

def getCourseMembers (request,id):
	pass

def checkAuth (request):
	try:
		m_id=request.session['member_id']
	except KeyError:
		return False
	return m_id

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
			request.session['member_id'] = usr.id
			request.session.set_expiry(0)
			return HttpResponseRedirect(reverse('courses:index'))
		else: 
			return render(request, "courses/form.html", context)

def logOut(request):
	try:
		m_id=request.session['member_id']
	except KeyError:
		return render(request, "courses/index.html")
	else:
		m= Member.objects.get(pk=m_id)
		m.logged_in=False
		m.save()
		del request.session['member_id']
		return render(request, "courses/index.html")

def signUp(request):
	fname = request.POST['firstname']
	lname = request.POST['lastname']
	mail = request.POST['emailsignup']
	password = request.POST['passwordsignup']
	pwd2 = request.POST['passwordsignup_confirm']
	u_img = request.FILES['img']
	context={}

	if (password != pwd2):
		context['wrong']=True
		return render(request, "courses/form.html", context)
	else:
		mem = Member.objects.create(first_name=fname, last_name=lname, email=mail, pwd=password, logged_in=True,)
		mem.img=(u_img)
		mem.save()
		return HttpResponseRedirect(reverse('courses:index'))
		#need to login
def postComment(request, course_id):
	c=Course.objects.get(pk=course_id)
	m=Member.objects.get(pk=request.session['member_id'])
	name=m.first_name+" "+m.last_name
	com=Comment(content=request.POST['text'],title=name, course=c)
	c.save()
	com.save()

	return HttpResponseRedirect(reverse('courses:about',kwargs={'course_id':course_id}))



