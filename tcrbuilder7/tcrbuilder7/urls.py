"""
URL configuration for tcrbuilder7 project.
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("projects/", views.project, name="projects"),
    path("contact/", views.contact, name="contact"),

    # --- NEW SERVICE PAGE URLS ---
    path("planning/", views.planning, name="planning"),
    path("construction/", views.construction, name="construction"),
    path("interior-designing/", views.interior, name="interior"),
    path("exterior-designing/", views.exterior, name="exterior"),

    # --- NECESSARY URL FOR PROJECT RATING ---
    path("rate/<int:project_id>/", views.submit_rating, name="submit_rating"),
]

# Media file handling for project images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)