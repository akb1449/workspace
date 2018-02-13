from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    institution_name = models.CharField(max_length=128, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    degree = models.CharField(max_length=255, null=False, blank=True)
    major = models.CharField(max_length=64, null=False, blank=True)
    gpa = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.title
