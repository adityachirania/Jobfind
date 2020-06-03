from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewJobForm

# Create your views here.

def homepage(request):
    if request.user.is_authenticated:
        return redirect("jobfinder:home")
    return render(request = request,template_name = "jobfinder/homepage.html")

def register(request):

    if request.user.is_authenticated:
        return redirect("jobfinder:home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("jobfinder:login")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "jobfinder/register.html",
                          context={"form":form})
    form = UserCreationForm
    return render(request = request,
                  template_name = "jobfinder/register.html",
                  context={"form":form})

def login_request(request):
    if request.user.is_authenticated:
        return redirect("jobfinder:home")
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}")
                return redirect('jobfinder:home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "jobfinder/login.html",
                    context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("jobfinder:homepage")

def home(request):
    if request.user.is_authenticated:
        context = {
            "user":request.user
        }
        return render(request = request,template_name = "jobfinder/home.html",context = context)
    else:
        return redirect("jobfinder:login")

# def add_job(request):
#     form = NewJobForm()
#     return render(request, 'jobfinder/job_edit.html', {'form': form})



