from django.shortcuts import render, redirect
from . models import Form
# Create your views here.

def home(request):
    
    if request.method == "POST":
        name = request.POST.get('username')
        subject = request.POST.get('subject')
        age = request.POST.get('age')
        data = Form(username=name, subject=subject, age=age)
        data.save()
        
        return redirect('student_data_list')
    
    return render(request, 'home.html')

def student_data(request):
    data_1 = Form.objects.all()
    context = {
    'data':data_1
    }
    return render(request, 'student_entry.html', context)

def about(request):
    
    return render(request, 'about.html')

def service(request):
    
    return render(request, 'service.html')

def Teacher(request):
    
    return render(request, 'teacher.html')

def Result(request):
    
    return render(request, 'result.html')