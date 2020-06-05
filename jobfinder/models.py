from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField( max_length=10)
    Address = models.CharField(max_length=200)

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'

    def __str__(self):
        """Convert entry of class Employee to a string representation."""
        return "{}".format(self.Username)


class Category(models.Model):
    Tag = models.CharField(max_length=30)
    Characteristics = models.ManyToManyField(
        Profile, through="SkillSet", through_fields=("CategoryTags","Profile"),
    )

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        """Convert entry of class Employee to a string representation."""
        return "{}".format(self.Tag)

class SkillSet(models.Model):
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    CategoryTags = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Skill Sets'
        verbose_name = 'Skill Set'
    

class Job(models.Model):
    TYPE_CHOICES=[
        ("Skilled","Skilled"),
        ("Unskilled","Unskilled")
        ]
    Poster = models.ForeignKey(Profile,on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Type = models.CharField(choices=TYPE_CHOICES, max_length=10)
    Descripton = models.CharField(max_length=500)
    Assigned = models.BooleanField()
    ApplyBy = models.DateField()
    Characteristics = models.ManyToManyField(
        Category, through="JobCategory", through_fields=("Job", "Category"),
    )

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Jobs'
        verbose_name = 'Job'

    def __str__(self):
        """Convert entry of class Employee to a string representation."""
        return "{}".format(self.Title)

class JobCategory(models.Model):
    Job = models.ForeignKey(Job,on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Job-Category connections'
        verbose_name = 'Job-category connection'

    def __str__(self):
        """Convert entry of class Employee to a string representation."""
        return "{}-{}".format(self.Job.Title,self.Category.Tag)

class JobConnection(models.Model):
    Jobid =    models.ForeignKey(Job,on_delete=models.CASCADE)
    Employee = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='employee')
    Completed = models.BooleanField()

    class Meta:
        """Declare the metadata of the model"""
        verbose_name_plural = 'Job Connections'
        verbose_name = 'Job Connection'


