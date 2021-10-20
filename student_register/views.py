from django.shortcuts import redirect, render
from .forms import Register_form
from .models import Register



# Create your views here.
def home (request):
    return render(request, "student_register/base.html")

def student_form(request):
    form = Register_form()
    
    if request.method == "POST":
        form = Register_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form" : form
    }
    return render (request, "student_register/student_form.html",context)

def student_list(request):
    
    students = Register.objects.all()
    
    context = {
        "students" : students
    }
    return render (request, "student_register/student_list.html",context)