from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from Home.models import Story,Fest
# Create your views here.
def home(request):
	stories = Story.objects.all()
	festivals = Fest.objects.all()
	context = {'stories' : stories , 'festival' : festivals}
	return render(request,'home.html',context)

def aboutus(request):
	return render(request,'about.html')

def contactus(request):
	return render(request,'contact.html')

def signin(request):
	if request.method=="POST":
		if 'register' in request.POST:
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			username = request.POST.get('username')
			password = request.POST.get('password')
			email = request.POST.get('email')

			user= User.objects.filter(username=username)

			if user.exists():
				messages.error(request, "Username already exist")
				return redirect('signin')

			user = User.objects.create(
				first_name=first_name,
				last_name=last_name,
				username=username
			)

			user.set_password(password)
			user.save()
			messages.info(request, "Account created successfully")
			# return redirect('login')
			if user is not None:
				login(request, user)
				messages.info(request, "Account created successfully")
				return redirect('home')
			else:
				messages.error(request, "There was an issue logging in")
				return redirect('signin')


		elif 'login' in request.POST:
			username = request.POST.get('username')
			password = request.POST.get('password')

			if not User.objects.filter(username = username).exists():
				messages.error(request, "Invaild Username")
				return redirect('signin')

			user = authenticate(username=username, password=password)

			if user is None :
				messages.error(request, "Invaild Password")
				return redirect('signin')
			else:
				login(request, user)
				return redirect('home')	
	return render(request,'signin.html')

def index(request):
	return render(request,'index.html')

def logout_page(request):
	logout(request)
	return redirect("home")