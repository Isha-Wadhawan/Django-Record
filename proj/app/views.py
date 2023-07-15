from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import studentForm
from .models import Student 
# Create your views here.
def base(request):
    if request.method == "POST":
        form  = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/display/")
    else:
        form = studentForm()
        return render(request, 'base.html', {'form': form})
    
def display(request):
    rec = Student.objects.all()
    return render (request, 'display.html', {'rec': rec})

def delete(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        Student.objects.filter(name=nam).delete()
        return redirect('/display/')
    else:
        return render(request, 'delete.html')

def about(request):
    return render(request,'about.html')