from django.shortcuts import render
from .models import Blogs
# Create your views here.

def home(request):
    return render (request,'layout.html')



def blog_views(request):
    blogs=Blogs.objects.only('blog_name','blog_img','text').order_by('-created_at')
    return render(request,'blogs.html',{'blogs':blogs})