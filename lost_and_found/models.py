from django.db import models

class LostItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_reported = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='lost_items/', null=True, blank=True)
    status = models.CharField(max_length=20, default='lost')

    def __str__(self):
        return f"Lost: {self.title}"

class FoundItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_reported = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='found_items/', null=True, blank=True)
    status = models.CharField(max_length=20, default='found')

    def __str__(self):
        return f"Found: {self.title}"
