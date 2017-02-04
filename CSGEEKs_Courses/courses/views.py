from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from courses.models import *
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
import os 
from PIL import Image, ImageOps, ImageDraw


# Create your views here.
def index (request):
	li = Course.objects.all()
	try:
		request.session['member_id']
	except KeyError:
		log=False
		context={'courses':li, 'log':log}
	else:
		m = Member.objects.get(pk=request.session['member_id'])
		log=True 
		context={'courses':li, 'log':log, 'member':m}
		

	
	return render(request, "courses/courses.html", context)

def getCourseAbout (request, course_id):
	data =checkAuth(request)
	if(data!=False):
		m = Member.objects.get(pk=request.session['member_id'])
		name = Course.objects.get(pk=course_id).title
		Posts=Course.objects.get(pk=course_id).post_set.all()
		Notis=Course.objects.get(pk=course_id).notification_set.all()

		# coms=Course.objects.get(pk=course_id).comment_set.all()
		context={'post':Posts, 'not':Notis,'cid':course_id ,'member':m}
		return render(request, "courses/about.html",context)
	else:
		return render(request, 'courses/form.html')

def getCourseware(request,course_id,video_id):
	m = Member.objects.get(pk=request.session['member_id'])
	videos=Course.objects.get(pk=course_id).video_set.all()
	current=Video.objects.get(pk=video_id)
	coms=Video.objects.get(pk=video_id).comment_set.all()
	context={'videos':videos, 'current':current, 'cid':course_id, 'vid':current, 'coms':coms , 'member':m}

	return render(request, "courses/courseware.html",context)

def getCourseAssig (request,course_id,agn_id):
	assigns=Course.objects.get(pk=course_id).assignment_set.all()
	current=Assignment.objects.get(pk=agn_id)
	m = Member.objects.get(pk=request.session['member_id'])
	context={'assigns':assigns, 'current':current, 'cid':course_id, 'aid':agn_id,'member':m}

	return render(request, "courses/assignments.html",context)

def getCourseMembers (request,course_id):
	students=Course.objects.get(pk=course_id).members.all()
	m = Member.objects.get(pk=request.session['member_id'])
	context={'members':students, 'cid':course_id,'member':m}

	return render(request, "courses/members.html",context)

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
		request.session['member_id'] = mem.id
		request.session.set_expiry(0)
		mem.img=(u_img)
		mem.save()
		file ,ext  = os.path.splitext(mem.img.path)
		size = (60,60)
		mask = Image.new('L', size, 0)
		draw = ImageDraw.Draw(mask) 
		draw.ellipse((0, 0) + size, fill=255)
		im = Image.open(mem.img.path)
		output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
		output.putalpha(mask)
		output.save(file + "-thumbnail"+".png")
		return HttpResponseRedirect(reverse('courses:index'))
		

def postComment(request, course_id, video_id):
	c=Course.objects.get(pk=course_id)
	v=Video.objects.get(pk=video_id)
	m=Member.objects.get(pk=request.session['member_id'])
	name=m.first_name+" "+m.last_name
	com=Comment(content=request.POST['text'],title=name,video=v)
	c.save()
	v.save()
	com.save()

	return HttpResponseRedirect(reverse('courses:ware',kwargs={'course_id':course_id, 'video_id':video_id}))

def getDashboard(request):
	data =checkAuth(request)
	if(data!=False):
		m_course =  Member.objects.get(pk=request.session['member_id']).course_set.all()
		name =  Member.objects.get(pk=request.session['member_id'])
		cont = {'courses':m_course ,'member':name}
		return render(request, "courses/dashboard.html",cont)
	else:return render(request, 'courses/form.html')

def uploadFile(request, course_id, agn_id):
	data=request.FILES['file']
	member=Member.objects.get(pk=request.session['member_id'])
	assign=Assignment.objects.get(pk=agn_id)
	File.objects.create(data=data, member=member, assign=assign)

	return HttpResponseRedirect(reverse('courses:agn',kwargs={'course_id':course_id, 'agn_id':agn_id}))



