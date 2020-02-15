from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField( max_length=10)
    Address = models.CharField(max_length=200)

class Category(models.Model):
    Tag = models.CharField(max_length=30)
    Characteristics = models.ManyToManyField(
        Profile, through="SkillSet", through_fields=("CategoryTags","Profile"),
    )

class SkillSet(models.Model):
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    CategoryTags = models.ForeignKey(Category,on_delete=models.CASCADE)
    

class Job(models.Model):
    TYPE_CHOICES=[
        ("Skilled","Skilled"),
        ("Unskilled","Unskilled")
        ]
    Poster = models.ForeignKey(Profile,on_delete=models.CASCADE)
    Type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    Descripton = models.CharField(max_length=500)
    Assigned = models.BooleanField()
    ApplyBy = models.DateField()
    Characteristics = models.ManyToManyField(
        Category, through="JobCategory", through_fields=("Job", "Category"),
    )

class JobCategory(models.Model):
    Job = models.ForeignKey(Job,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

class JobConnection(models.Model):
    Jobid =    models.ForeignKey(Job,on_delete=models.CASCADE)
    Employer = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='employer')
    Employee = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='employee')
    Completed = models.BooleanField()



