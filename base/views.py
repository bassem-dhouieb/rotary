from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Post, Member,Category,Project,Donation
from .forms import ContactForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.contrib import messages





# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('date').reverse()
    projects = Project.objects.all().order_by('date').reverse()
    donations = Donation.objects.all().order_by('title').reverse()
    context = {'posts':posts[:2],'projects':projects[:4],'donations':donations[:6]}
    return render(request,'base/index.html',context)

def about(request):
    members = Member.objects.all()
    context = {'members' : members}
    return render(request,'base/about.html',context)

def team(request):
    members = Member.objects.all()
    context = {'members':members}
    return render(request,'base/our-volunteer.html',context)


@csrf_exempt
def contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email_message = f"From: {first_name} {last_name} <{email}>\n\nSubject: {subject}\n\n{message}"
            if send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.EMAIL_HOST_USER]):
                error = "Your message has been sent."
            else:
                error = "Please try again."
        else:  
            error = "There was an error with your message. Please try again."
        return render(request, 'base/success.html',{'error':error})


    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'base/contact-us.html', context)

        



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
    q= request.GET.get('q','') 
    donations = Donation.objects.filter(
        Q(title__icontains=q)|
        Q(categories__name__icontains=q)|
        Q(content__icontains=q)
    ).order_by('title')
    unique_donation=[]
    seen_titles = set()
    for donation in donations:
            if donation.title not in seen_titles:
                unique_donation.append(donation)
                seen_titles.add(donation.title)
    
    paginator = Paginator(unique_donation, 6)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    categories = Category.objects.all().order_by('name')
    context = {'categories':categories,'page': page,'q':q}
    return render(request,'base/donations.html',context)

def donation(request,pk):
    q= request.GET.get('q','') 
    donation = Donation.objects.get(slug=pk)
    categories = Category.objects.all().order_by('name')
    context = {'donation': donation,'q':q,'categories':categories}

    return render(request,'base/donation.html',context)