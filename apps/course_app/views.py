from django.shortcuts import render, HttpResponse, redirect
from apps.course_app.models import *

def index(request):
    print(Course.objects.all().values())
    variable =  Course.objects.all().values()
    return render(request,'course_app/index.html', {'variable':variable})
def add(request):
    Course.objects.create(name=request.POST['name'], desc = request.POST['desc'])
    return redirect('/courses')
def destroy(request,id):
    info =  Course.objects.get(id=id)
    request.session['id'] = id
    return render(request,'course_app/destroy.html', {'info':info})
def delete(request):
    b = Course.objects.get(id=request.session['id'])
    b.delete()
    return redirect('/courses')