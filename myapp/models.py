from django.db import models



class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name



# models.py

from django.db import models


class Career(models.Model):

    JOB_TYPES = (

        ('full-time', 'Full Time'),

        ('part-time', 'Part Time'),

        ('internship', 'Internship'),

    )

    title = models.CharField(max_length=200)

    location = models.CharField(max_length=200)

    job_type = models.CharField(max_length=50, choices=JOB_TYPES)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title