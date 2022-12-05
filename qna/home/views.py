from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from home.models import OurUser
from questions.models import Questions
from category.models import Category
from answer.models import Answer
# Create your views here.
def home_view(request):
    user_email = OurUser.objects.all()
    print(user_email)
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0
    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 10):
                    if(c == 1):
                        print(user_email[i])
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        print(user_info)
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break

    print(user_list)

    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1       
    perchantage = (total_answer / total_question) * 100


    if request.session['active'] == True:
        print("session available")
        my_user = OurUser.objects.filter(email = request.session['0'])
        return render(request,"index.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})
    else:
        print("sorry session not available")
        return render(request,"index.html",{"questions" : questions,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})

def about(request):
    return render(request,"about.html")

def profile_view_other(request,u):
    user = OurUser.objects.all().filter(user = u)
    if(user[0].email == request.session['0']):
        return HttpResponseRedirect("/profile")
    else:
        questions = Questions.objects.all().filter(u_email = user[0].email)
        answers = Answer.objects.all().filter(u_email = request.session['0'])
 
        
        return render(request,"othersprofile.html",{"user": user[0],"questions" : questions})

def profile_view_other_answer(request,u):
    user = OurUser.objects.all().filter(user = u)
    if(user[0].email == request.session['0']):
        return HttpResponseRedirect("/profile")
    else:
        questions = Questions.objects.all().filter(u_email = user[0].email)
        answers = Answer.objects.all().filter(u_email = user[0].email)
        q=[]
        for i in range(len(answers)):
            q.append(answers[i].Q_ID)
            q2 = Questions.objects.filter(id = answers[i].Q_ID)
        q50 = Questions.objects.filter(id__in = q)


        
        return render(request,"othersprofile2.html",{"user": user[0],"questions" : questions,"answered_question" : q50})    

def show_answer_view(request,id):
    user_email = OurUser.objects.all()
    print(user_email)
    
    user_list={}
    questions_info = Questions.objects.all()
    count=0
    for i in range(0,len(user_email)):
        user_info = {}
        c = 0
        for j in range(0,len(questions_info)):
            if(user_email[i].email == questions_info[j].u_email):
                c+=1
                if(count != 10):
                    if(c == 1):
                        print(user_email[i])
                        user_info['name'] = user_email[i].name
                        user_info['img'] = user_email[i].img
                        user_info['user'] = user_email[i].user
                        print(user_info)
                        user_list[i] = user_info
                        
                        count+=1
                    else:
                        break
                else:
                    break

    print(user_list)

    questions = Questions.objects.all()
    total_question = len(questions)
    answer = Answer.objects.all()
    total_answer = 0

    for i in range(0,total_question):
        for j in range(0,len(answer)):
            if questions[i].id == int(answer[j].Q_ID):
                total_answer=total_answer + 1       
    perchantage = (total_answer / total_question) * 100
    if(request.method == 'POST'):
        answer = request.POST['answer']
        a = Answer(Q_answer = answer, like = 0, dislike = 0,u_email = request.session['0'],Q_ID = id)
        a.save()
    else:      
        ques = Questions.objects.filter(id = id)
        ans = Answer.objects.all().filter(Q_ID = id)
        if request.session['active'] == True:
            print("session available")
            my_user = OurUser.objects.filter(email = request.session['0'])
            return render(request,'answer.html',{"question": ques[0],"my_users" : my_user[0], "registered" : True,"answers" : ans,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})
        else:
            return render(request,'answer.html',{"question": ques[0],"answers" : ans,"total_question":total_question,"total_answer" : total_answer,"perchantage" : perchantage,"user_list" : user_list})


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
                request.session['active'] = True
                return HttpResponseRedirect("/")

            else:
                print("not login")
                return HttpResponseRedirect("/login")

        else:
            print("email not available")
            return HttpResponseRedirect("/login")

    else:
        return render(request, "Login.html")

def logout(request):
    del request.session['0']
    request.session['active'] = False
    request.session.modified = True
    return HttpResponseRedirect("/")

def recover(request):
    return render(request, "Recover.html")

def ask_question_view(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        details = request.POST['details']
        category = request.POST['category']
        q = Questions(title = title , details = details,u_email = request.session['0'],cat_name = category)
        q.save()
        return HttpResponseRedirect("/")
    else:
        if request.session['active'] == True:
            print("session available")
            category = Category.objects.all()
            my_user = OurUser.objects.filter(email = request.session['0'])
            return render(request,"askquestion.html",{"my_users" : my_user[0], "registered" : True, "category" : category})
        else:
            print("sorry session not available")
            return HttpResponseRedirect("/login")

def pagination_view(request):
    return HttpResponse('Hello pagination  page')

def profile_view(request):
    if request.session['active'] == True:
        print("session available")
        print(request.session["0"])
        questions = Questions.objects.all().filter(u_email = request.session['0'])
        answers = Answer.objects.all().filter(u_email = request.session['0'])
        q=[]
        for i in range(len(answers)):
            q.append(answers[i].Q_ID)
            q2 = Questions.objects.filter(id = answers[i].Q_ID)
        q50 = Questions.objects.filter(id__in = q)
        print(q50)
        print(q)
        # q = []
        q_title = []

        #     q_title.append(q2[0].title)
        # print(q)
        # print(q_title)
        # print(questions)
        my_user = OurUser.objects.filter(email = request.session['0'])
        print(len(q))
        length = []
        for i in range(0,len(q)):
            length.append(i)
        print(length)
        return render(request,"profile.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions,"answers" : answers, "answered_question" : q50})
    else:
        print("sorry session not available")
    return render(request,'profile.html')

def profile_view_answer(request):
    if request.session['active'] == True:
        print("session available")
        print(request.session["0"])
        questions = Questions.objects.all().filter(u_email = request.session['0'])
        answers = Answer.objects.all().filter(u_email = request.session['0'])
        q=[]
        for i in range(len(answers)):
            q.append(answers[i].Q_ID)
            q2 = Questions.objects.filter(id = answers[i].Q_ID)
        q50 = Questions.objects.filter(id__in = q)
        print(q50)
        print(q)
        # q = []
        q_title = []

        #     q_title.append(q2[0].title)
        # print(q)
        # print(q_title)
        # print(questions)
        my_user = OurUser.objects.filter(email = request.session['0'])
        print(len(q))
        length = []
        for i in range(0,len(q)):
            length.append(i)
        print(length)
        return render(request,"profile2.html",{"my_users" : my_user[0], "registered" : True,"questions" : questions,"answers" : answers, "answered_question" : q50})
    else:
        print("sorry session not available")
    return render(request,'profile.html')

def profile_setting_view(request):
    return HttpResponse('Hello profile setting page')


def category_view(request):
    return HttpResponse('Hello category page')

def tag_view(request):
    return HttpResponse('Hello tag page')