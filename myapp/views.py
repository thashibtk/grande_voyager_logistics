from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):

    if request.method == 'POST' and 'email' in request.POST:
        email = request.POST.get('email').strip()
        if email:
            if not Newsletter.objects.filter(email=email).exists():
                Newsletter.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email address.")
        return redirect(request.META.get('HTTP_REFERER', '/'))

    blogs = Blog.objects.all()[:3]
    services_nav = Services.objects.all().order_by('priority')
    services = Services.objects.all().order_by('priority')

    context = {
        "blogs":blogs,
        "services_nav":services_nav,
        "services":services,
    }
    return render(request, "home.html", context)

def about(request):
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services_nav":services_nav,
    }
    return render(request, "about.html", context)

def services(request):
    services = Services.objects.all().order_by('priority')
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services":services,
        "services_nav":services_nav,
    }
    return render(request, "services.html", context)

def service_detail(request, pk):
    service = Services.objects.get(slug=pk)
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "service":service,
        "services_nav":services_nav,
    }
    return render(request, "service_detail.html", context)

def facilities(request):
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services_nav":services_nav,
    }
    return render(request, "facilities.html", context)

def certificates(request):
    certificates = Certificates.objects.all()
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "certificates":certificates,
        "services_nav":services_nav,
    }
    return render(request, "certificates.html", context)

def blog(request):
    blogs = Blog.objects.all()
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "blogs":blogs,
        "services_nav":services_nav,
    }
    return render(request, "blog.html", context)

def blog_detail(request, pk):
    blog = Blog.objects.get(slug=pk)
    blogs = Blog.objects.all()[:3]
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "blog":blog,
        "blogs":blogs,
        "services_nav":services_nav,
    }
    return render(request, "blog_detail.html", context)

def contact(request):
    services_nav = Services.objects.all().order_by('priority')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, phone=phone, message=message)

    context = {
        "services_nav":services_nav,
    }
    return render(request, "contact.html", context)
