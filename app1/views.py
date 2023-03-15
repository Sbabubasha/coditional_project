from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':300,'b':200,'c':2500}
    return render(request,'condition.html',d)