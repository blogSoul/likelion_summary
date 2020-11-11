from django.shortcuts import render

# Create your views here.
def profile_home(request):
    return render(request,'profile_home.html')

def profile_blog(request):
    return render(request, 'profile_blog.html')

def profile_comment(request):
    return render(request, 'profile_comment.html')