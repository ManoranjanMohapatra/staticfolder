from django.shortcuts import render

# Create your views here.
def insert_image(request):
    return render(request,'image.html')