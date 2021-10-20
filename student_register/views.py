from django.shortcuts import render
from .forms import Register_form
from .models import Register

# Create your views here.
def student_form(request):
    form = Register_form()
    context = {
        "form" : form
    }
    return render (request, "student_register/student_form.html",context)

def student_list(request):
    student = Register.objects.all()
    
    context = {
        "student" : student
    }
    return render (request, "student_register/student_list.html",context)