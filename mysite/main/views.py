from django.shortcuts import render
from .models import TestImage

# Create your views here.
def home(request):
    testimage = TestImage.objects.all()
    context = {'testimage': testimage}
    return render(request, 'main/home.html', context)

def about(request):
    return render(request, "main/about.html")