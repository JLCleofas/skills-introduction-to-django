from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    STATUS_CHOICES = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.title