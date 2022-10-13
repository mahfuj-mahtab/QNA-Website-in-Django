from django.shortcuts import render,HttpResponse

# Create your views here.
def home_view(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def show_answer_view(request):
    return HttpResponse('Hello show answer  page')


def search_view(request):
    return HttpResponse('Hello search page')

def signup_view(request):
    return HttpResponse('Hello signup/login page')

def ask_question_view(request):
    return HttpResponse('Hello ask question page')

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