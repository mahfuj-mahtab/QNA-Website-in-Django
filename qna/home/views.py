from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from home.models import OurUser

# Create your views here.
def home_view(request):
    print(request.session['0'])
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def show_answer_view(request):
    return render(request,'answer.html')


def search_view(request):
    return HttpResponse('Hello search page')

def signup_view(request):
    if(request.method == "POST"):
        name = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        emailcount = OurUser.objects.all().filter(email = email)

        if(len(emailcount) > 0):
            print("More than one email")
        else:
            usercount = OurUser.objects.all().filter(user = username)
            if(len(usercount) > 0):
                print("more than one user name")
            else:
                if(len(password) >= 8):
                    user = OurUser(name = name, email = email,password = password,user = username,Num_of_followers = 0,Num_of_following = 0,img = "default.jpg",phone_No = 0,Bio = '')
                    user.save()
                    return HttpResponseRedirect("/")
                else:
                    print("password is less than 8 char")
       
        
        
    else:
        return render(request, "Register.html")

def login(request):
    if(request.method == 'POST'):
        email = request.POST['email']
        password = request.POST['password']
        ecount = OurUser.objects.all().filter(email = email)
        if(len(ecount) == 1):
            if(ecount[0].password == password):
                print("login")
                request.session[0] = email
                return HttpResponseRedirect("/")

            else:
                print("not login")
                return HttpResponseRedirect("/login")

        else:
            print("email not available")
            return HttpResponseRedirect("/login")

    else:
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