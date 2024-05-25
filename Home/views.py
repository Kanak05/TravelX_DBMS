from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return render(request,'index.html')

def aboutus(request):
	return render(request,'about.html')

def contactus(request):
	return render(request,'contact.html')