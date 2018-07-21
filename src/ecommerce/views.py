from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

def home_page(request):
	context = {
	"title" : "home page",
	"content" : "welcome to home page"
	}
	if request.user.is_authenticated:
		context["premium_content"] = "its premium content"
	return render(request,"home_page.html",context)

def about_page(request):
	context = {
	"title" : "about page",
	"content" : "welcome to about page"
	}

	return render(request,"home_page.html",context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	"title" : "contact page",
	"content" :  "welcome to contact page",
	"form"	  : contact_form
	}

	if contact_form.is_valid():
		print(contact_form.cleaned_data)

	if request.method == "POST":
		# print(request.POST)
		print(request.POST.get("fullname"))
		print(request.POST.get("email"))
		print(request.POST.get("content"))

	return render(request,"contact/view.html",context)

def login_page(request):
	login_form = LoginForm(request.POST or None)
	print("user logged in")
	# print(request.user.is_authenticated())
	context = {
	"form" : login_form
	}
	if login_form.is_valid():
		print (login_form.cleaned_data)
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		print(user)
		if user is not None:
			# print(request.user.is_authenticated())
			# context['form'] = LoginForm()
			login(request, user)
			return redirect("/login")
		else:
			print ("error")
	return render(request,"auth/login.html",context)


User = get_user_model()
def register_page(request):
	register_form = RegisterForm(request.POST or None)
	context = {
	"form" : register_form
	}

	if register_form.is_valid():
		# print(register_form.cleaned_data)
		username = register_form.cleaned_data.get("username")
		email	 = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		# password2 = register_form.cleaned_data.get("password2")
		new_user = User.objects.create_user(username, email, password)
		# print(username)

	return render(request,"auth/login.html",context)