from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from.form import StudentForm
from .models import Department,Course,Student
from django.http import JsonResponse

# Create your views here.
def hom(request):

    return render(request,'hom.html')

def log(request):
    if request.method=='POST':
       username = request.POST['username']
       password = request.POST['password1']
       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           return redirect('form')
       else:
           messages.info(request, "inavlid details")
           return redirect("log")
    return render(request,'login.html')
def reg(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
          if User.objects.filter(username=username).exists():
              messages.info(request,"username already taken")
              return redirect('reg')
          elif User.objects.filter(email=email).exists():
              messages.info(request,"email already taken")
              return redirect('reg')
          else:
             user=User.objects.create_user(username=username,email=email,password=password)
             user.save();
             print("user created")
             return redirect("log")
        else:
            messages.info(request,"password not match")
            return redirect('reg')
        return redirect('/')

    return render(request,'registration.html')

def form(request):
    form = StudentForm()
    if request.method == 'POST' :
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Successful")
            # return redirect()

    return render(request,'form.html', {'form': form})

def load_courses(request):
    department_id=request.GET.get('department_id')
    courses=Course.objects.filter(department_id=department_id).all()
    # return render(request,'course_op.html',{'course':courses})
    return JsonResponse(list(courses.values('id', 'name')), safe=False)

def logout(request):
    auth.logout(request)
    return redirect('hom')

def cs(request,id):
    if id==1:
        return render(request, 'cs.html',{'id':id})
    if id==2:
        return render(request, 'bio.html',{'id':id})
    if id==3:
        return render(request, 'phy.html',{'id':id})
    if id==4:
        return render(request, 'comm.html',{'id':id})
    if id==5:
        return render(request, 'huma.html',{'id':id})


