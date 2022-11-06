from django.shortcuts import render, HttpResponse
from home.models import OurUser

# Create your views here.
def home_view(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def show_answer_view(request):
    return render(request,'answer.html')


def search_view(request):
    return HttpResponse('Hello search page')

def signup_view(request):
    if(request.method == "POST"):
        user = OurUser(name = request.POST['fullname'], email = request.POST['email'])
        user.save()
        
        
    else:
        return render(request, "Register.html")

def login(request):
    return render(request, "Login.html")

def recover(request):
    return render(request, "Recover.html")

def ask_question_view(request):
    return render(request,"askquestion.html")

def pagination_view(request):
    return HttpResponse('Hello pagination  page')

def profile_view(request):
    return HttpResponse('Hello profile page')

def profile_setting_view(request):
    return HttpResponse('Hello profile setting page')


def category_view(request):
    return HttpResponse('Hello category page')

def tag_view(request):
    return HttpResponse('Hello tag page')