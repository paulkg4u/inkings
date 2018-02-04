from django.shortcuts import render

# Create your views here.


def homeView(request):
    return render(request,'index.html', {},)

def taskDetails(request, uuid):
    pass

def filterTasks(requset):
    pass