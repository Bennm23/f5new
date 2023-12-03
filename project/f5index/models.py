from django.urls import reverse
from django.db import models

class SupportSubmission(models.Model):
    email = models.EmailField()
    cell = models.CharField(max_length=15)  # You may adjust the max_length according to your needs
    message = models.TextField()

    def __str__(self):
        return f"Support Submission - {self.email}"
