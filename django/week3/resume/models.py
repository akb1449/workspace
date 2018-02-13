from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return "{}{}{}".format(self.title, self.location, self.description)

class Education(models.Model):
    institution_name = models.CharField(max_length=128, null=False, blank=False)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    gpa = models.FloatField(default=0.0)

    def __str__(self):
        return "{}{}{}".format(self.institution_name, self.degree, self.major)
