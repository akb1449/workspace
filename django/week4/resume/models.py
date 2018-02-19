from django.db import models

# Create your models here.
class Resume(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    
    def get_last_name_first_name(self):
        return "{} {}".format(self.last_name, self.first_name)
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    def get_experience(self):
        return self.experience_set.all()
    def get_education(self):
        return self.education_set.all()

class Experience(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=64, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)

    def __str__(self):
        return "{}{}{}".format(self.title, self.location, self.description)

class Education(models.Model):
    parent_resume = models.ForeignKey('Resume', on_delete=models.CASCADE, default=1)
    institution_name = models.CharField(max_length=128, null=False, blank=False)
    location = models.CharField(max_length=255)
    degree = models.CharField(max_length=128)
    major = models.CharField(max_length=128)
    gpa = models.FloatField(default=0.0)

    def __str__(self):
        return "{}{}{}".format(self.institution_name, self.degree, self.major)
