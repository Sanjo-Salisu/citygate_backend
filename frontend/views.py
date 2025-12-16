from django.shortcuts import render
from management.models import Career
from management.models import ManagementProfile
from management.models import GalleryImage
from django.core.mail import send_mail
from django.http import HttpResponse

def index(request):
    return render(request, "frontend/index.html")

def about(request):
    profiles = ManagementProfile.objects.all()
    return render(request, 'frontend/about.html', {'profiles': profiles})

def loan(request):
    return render(request, "frontend/loan.html")

def FAQ(request):
    return render(request, "frontend/FAQ.html")

def career(request):
    careers = Career.objects.all().order_by('-created_at')  # latest first
    return render(request, "frontend/career.html", {"careers": careers})

def contact(request):
    return render(request, "frontend/contact.html")

def privacy(request):
    return render(request, "frontend/privacy.html")

def terms(request):
    return render(request, "frontend/terms.html")

def branch(request):
    return render(request, "frontend/branch.html")

def gallery_frontend(request):
    # Query images for each section
    first_section_images = GalleryImage.objects.filter(section='first').order_by('-created_at')
    second_section_images = GalleryImage.objects.filter(section='second').order_by('-created_at')
    third_section_images = GalleryImage.objects.filter(section='third').order_by('-created_at')

    context = {
        'first_section_images': first_section_images,
        'second_section_images': second_section_images,
        'third_section_images': third_section_images,
    }

    return render(request, 'frontend/gallery.html', context)

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def send_message(request):
    success_message = ""
    error_message = ""

    if request.method == "POST":
        print("POST received!")  # debug line
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        message = request.POST.get("message", "").strip()

        content = f"""
        Name: {full_name}
        Email: {email}
        Phone: {phone}

        Message:
        {message}
        """

        try:
            send_mail(
                subject="New Message From Website Contact Form",
                message=content,
                from_email="info@citygateglobal.com",
                recipient_list=["info@citygateglobal.com"],
                fail_silently=False,
            )
            print("Email sent successfully!")  # debug line
            success_message = "Your message has been sent successfully!"
        except Exception as e:
            print("Email failed:", e)
            error_message = f"Failed to send email: {e}"

    # Render the contact page template again, with optional messages
    return render(request, "frontend/contact.html", {
        "success_message": success_message,
        "error_message": error_message
    })

def set_cookie_view(request):
    """
    Display page and determine whether to load analytics based on cookie consent.
    """
    consent = request.COOKIES.get("cookie_consent")  # "accepted", "declined", or None

    # Determine if analytics can be loaded
    load_analytics = consent == "accepted"

    return render(request, "frontend/cookie.html", {
        "load_analytics": load_analytics,
        "cookie_consent": consent
    })

def contact_view(request):
    consent = request.COOKIES.get("cookie_consent")
    load_analytics = consent == "accepted"

    return render(request, "contact.html", {"load_analytics": load_analytics})

# Create your views here.
