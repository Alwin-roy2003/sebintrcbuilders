from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return "About Section"


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class Project(models.Model):
    name = models.CharField(max_length=200, default="New Project")
    description = models.TextField(blank=True)
    location = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)

    # Review Fields
    owner_email = models.EmailField(blank=True, null=True)
    reviewer_name = models.CharField(max_length=100, blank=True, null=True)  # THIS IS THE MISSING FIELD
    rating = models.PositiveSmallIntegerField(default=5)
    review_text = models.TextField(blank=True, null=True)
    has_review = models.BooleanField(default=False)

    def __str__(self):
        return self.name