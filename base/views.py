from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Member,Category,Project
from django.core.paginator import Paginator
from django.db.models import Q




# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('date').reverse()
    context = {'posts':posts[:2]}
    return render(request,'base/index.html',context)

def about(request):
    members = Member.objects.all()
    
    context = {'members' : members}
    return render(request,'base/about.html',context)

def team(request):
    members = Member.objects.all()

    context = {'members':members}
    return render(request,'base/our-volunteer.html',context)

def contact(request):
    return render(request,'base/contact-us.html')

def blogs(request):
    q= request.GET.get('q','') 
    posts = Post.objects.filter(
        Q(title__icontains=q)|
        Q(categories__name__icontains=q)|
        Q(content__icontains=q)
    ).order_by('-date', 'title')
    unique_post=[]
    seen_titles = set()
    for post in posts:
            if post.title not in seen_titles:
                unique_post.append(post)
                seen_titles.add(post.title)
    
    paginator = Paginator(unique_post, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    categories = Category.objects.all().order_by('name')
    context = {'categories':categories,'page': page,'posts':unique_post[:4],'q':q}
    return render(request,'base/blogs.html',context)

def blog(request,pk):
    post = Post.objects.get(slug=pk)
    post_images = post.postimage_set.all()
    categories = Category.objects.all().order_by('name')
    posts = Post.objects.all().order_by('date').reverse()

    context = {'post':post,'posts':posts[:4],'categories':categories,'post_images':post_images}
    return render(request,'base/blog.html',context)

def projects(request):
    q= request.GET.get('q','') 
    projects = Project.objects.filter(
        Q(title__icontains=q)|
        Q(location__icontains=q)|
        Q(categories__name__icontains=q)|
        Q(content__icontains=q)
    ).order_by('-date', 'title')
    unique_project=[]
    seen_titles = set()
    for project in projects:
            if project.title not in seen_titles:
                unique_project.append(project)
                seen_titles.add(project.title)
    
    paginator = Paginator(unique_project, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    categories = Category.objects.all().order_by('name')
    context = {'categories':categories,'page': page,'projects':unique_project[:4],'q':q}
    return render(request,'base/projects.html',context)

def project(request,pk):
    q= request.GET.get('q','') 
    project = Project.objects.get(slug=pk)
    project_images = project.projectimage_set.all()
    context = {'project': project,'q':q,'project_images':project_images}

    return render(request,'base/project.html',context)

def donations(request):
     return render(request,'base/donations.html')

def donation(request):
    return render(request,'base/donation.html')