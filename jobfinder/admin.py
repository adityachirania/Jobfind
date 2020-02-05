from django.contrib import admin
from .models import Profile
from .models import Category
from .models import SkillSet
from .models import Job
from .models import JobCategory

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(SkillSet)
admin.site.register(JobCategory)
admin.site.register(Job)
