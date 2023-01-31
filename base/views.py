from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Member,Category
from django.core.paginator import Paginator


posts = Post.objects.all().order_by('date').reverse()
categories = Category.objects.all().order_by('name')
members = Member.objects.all()
# Create your views here.
def index(request):
    return render(request,'base/index.html')

def about(request):
     return render(request,'base/about.html')

def team(request):
   
    context = {'members':members}
    return render(request,'base/our-volunteer.html',context)

def contact(request):
    return render(request,'base/contact-us.html')

def blogs(request):
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'categories':categories,'posts': page}
    return render(request,'base/blogs.html',context)

def blog(request,pk):
    post = Post.objects.get(slug=pk)
    context = {'post':post,'posts':posts[:4],'categories':categories}
    return render(request,'base/blog.html',context)