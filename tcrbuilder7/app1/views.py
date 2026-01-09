from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import About, Contact, Project


def home(request):
    """
    Home page view — displays all sections and handles contact form submission.
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        if name and email and message_text:
            Contact.objects.create(
                name=name,
                email=email,
                message=message_text,
                created_at=timezone.now()
            )
            try:
                send_mail(
                    subject=f"New Contact Message from {name}",
                    message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["alwinroycristiano@gmail.com"],
                    fail_silently=False,
                )
                messages.success(request, "✅ Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"❌ There was an issue sending your message: {e}")
        else:
            messages.warning(request, "⚠️ Please fill in all fields before submitting.")

        return redirect("/#contact")

    about_info = About.objects.first()
    projects = Project.objects.all()

    return render(request, "home.html", {
        "about": about_info,
        "projects": projects,
        "now": timezone.now(),
    })


def about(request):
    """
    About section — shows About data (same template)
    """
    about_info = About.objects.first()
    return render(request, "home.html", {
        "about": about_info,
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })


def services(request):
    """
    Services section — still same template
    """
    return render(request, "home.html", {
        "about": About.objects.first(),
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })


def project(request):
    """
    Projects section — displays all projects
    """
    projects = Project.objects.all()
    return render(request, "home.html", {
        "projects": projects,
        "about": About.objects.first(),
        "now": timezone.now(),
    })


def contact(request):
    """
    Contact form section — handles form submission only
    """
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_text = request.POST.get("message")

        if name and email and message_text:
            Contact.objects.create(
                name=name,
                email=email,
                message=message_text,
                created_at=timezone.now()
            )
            try:
                send_mail(
                    subject=f"New Contact Message from {name}",
                    message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=["alwinroycristiano@gmail.com"],
                    fail_silently=False,
                )
                messages.success(request, "✅ Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"❌ There was an issue sending your message: {e}")
        else:
            messages.warning(request, "⚠️ Please fill in all fields before submitting.")

        return redirect("/#contact")

    # GET request → show page
    return render(request, "home.html", {
        "about": About.objects.first(),
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })

# --- NEW SERVICE PAGE VIEWS ---

def planning(request):
    return render(request, "planning.html", {
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })

def construction(request):
    return render(request, "construction.html", {
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })

def interior(request):
    return render(request, "interior.html", {
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })

def exterior(request):
    return render(request, "exterior.html", {
        "projects": Project.objects.all(),
        "now": timezone.now(),
    })

# --- NECESSARY VIEW FOR PROJECT RATING ---

def submit_rating(request, project_id):
    if request.method == "POST":
        project_instance = get_object_or_404(Project, id=project_id)
        name = request.POST.get("name")
        email = request.POST.get("email")
        rating = request.POST.get("rating")
        review = request.POST.get("review")

        if project_instance.owner_email == email:
            project_instance.reviewer_name = name
            project_instance.rating = int(rating)
            project_instance.review_text = review
            project_instance.has_review = True
            project_instance.save()
            messages.success(request, "✅ Review published successfully!")
        else:
            messages.error(request, "❌ Email verification failed.")

    return redirect("/#projects")