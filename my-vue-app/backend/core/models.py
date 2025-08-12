
from django.db import models

class FeaturedProject(models.Model):
    CATEGORY_CHOICES = [
        ('WEBSITE', 'Website'),
        ('SOCIAL MEDIA', 'Social Media'),
        ('MARKETING', 'Marketing'),
        ('APP', 'App'),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField()

    def __str__(self):
        return self.title
