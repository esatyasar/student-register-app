from django.shortcuts import render
from .forms import Register_form

# Create your views here.
def student_form(request):
    form = Register_form()
    context = {
        "form" : form
    }
    return render (request, "student_register/student_form.html",context)