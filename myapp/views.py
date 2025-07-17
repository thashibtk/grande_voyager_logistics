from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse

def home(request):

    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST.get('email', '').strip()
            
            if email:
                try:
                    existing = Newsletter.objects.filter(email=email).exists()
                    
                    if not existing:
                        newsletter = Newsletter.objects.create(email=email)
                        messages.success(request, "Thank you for subscribing!")
                    else:
                        messages.info(request, "You are already subscribed.")
                        
                except Exception as e:
                    messages.error(request, "An error occurred. Please try again.")
            else:
                messages.error(request, "Please enter a valid email address.")
        
        return redirect('home')

    try:
        blogs = Blog.objects.all()[:3]
    except Exception as e:
        blogs = []
    
    try:
        services_nav = Services.objects.all().order_by('priority')
        services = Services.objects.all().order_by('priority')
    except Exception as e:
        services_nav = []
        services = []

    context = {
        "blogs": blogs,
        "services_nav": services_nav,
        "services": services,
    }
    
    return render(request, "home.html", context)



def test_newsletter(request):
    try:
        # Test creating a newsletter entry
        test_email = "test@example.com"
        Newsletter.objects.get_or_create(email=test_email)
        return HttpResponse("Newsletter model works!")
    except Exception as e:
        return HttpResponse(f"Newsletter model error: {e}")

# Rest of your views remain the same...
def about(request):
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services_nav": services_nav,
    }
    return render(request, "about.html", context)

def services(request):
    services = Services.objects.all().order_by('priority')
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services": services,
        "services_nav": services_nav,
    }
    return render(request, "services.html", context)

def service_detail(request, pk):
    service = Services.objects.get(slug=pk)
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "service": service,
        "services_nav": services_nav,
    }
    return render(request, "service_detail.html", context)

def facilities(request):
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "services_nav": services_nav,
    }
    return render(request, "facilities.html", context)

def certificates(request):
    certificates = Certificates.objects.all()
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "certificates": certificates,
        "services_nav": services_nav,
    }
    return render(request, "certificates.html", context)

def blog(request):
    blogs = Blog.objects.all()
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "blogs": blogs,
        "services_nav": services_nav,
    }
    return render(request, "blog.html", context)

def blog_detail(request, pk):
    blog = Blog.objects.get(slug=pk)
    blogs = Blog.objects.all()[:3]
    services_nav = Services.objects.all().order_by('priority')
    context = {
        "blog": blog,
        "blogs": blogs,
        "services_nav": services_nav,
    }
    return render(request, "blog_detail.html", context)

def contact(request):
    services_nav = Services.objects.all().order_by('priority')

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        try:
            Contact.objects.create(name=name, email=email, phone=phone, message=message)
            messages.success(request, "Thank you for your message!")
        except Exception as e:
            messages.error(request, "An error occurred. Please try again.")

    context = {
        "services_nav": services_nav,
    }
    return render(request, "contact.html", context)