from django.shortcuts import render

# Create your views here.
def student_form(request):
    return render (request, "student_register/student_form.html")