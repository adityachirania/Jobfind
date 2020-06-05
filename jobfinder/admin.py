from django.contrib import admin
from .models import Profile
from .models import Category
from .models import SkillSet
from .models import Job
from .models import JobCategory
from .models import JobConnection


admin.site.site_header = 'Jobfinder'

class profileAdmin(admin.ModelAdmin):
    list_display = ["Username", "FirstName", "LastName", "Address"]

class categoryAdmin(admin.ModelAdmin):
    list_display = ["id","Tag"]

class skillsetAdmin(admin.ModelAdmin):
    list_display = ["user", "CategoryTags"]

    def user(self,obj):
        return obj.Profile.Username

class jobAdmin(admin.ModelAdmin):
    list_display = ["poster","Descripton","Assigned","ApplyBy"]

    def poster(self,obj):
        return obj.Poster.Username

class jobcategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "tag"]

    def title(self,obj):
        return obj.Job.Title
    def tag(self,obj):
        return obj.Category.Tag

class jobconnectionAdmin(admin.ModelAdmin):
    list_display = ["title","poster","employee","Completed"]

    def poster(self,obj):
        return obj.Jobid.Poster.Username
    def title(self,obj):
        return obj.Jobid.Title
    def employee(self,obj):
        return obj.Employee.Username
    
# Register your models here.
admin.site.register(Profile,profileAdmin)
admin.site.register(Category,categoryAdmin)
admin.site.register(SkillSet,skillsetAdmin)
admin.site.register(JobCategory,jobcategoryAdmin)
admin.site.register(Job,jobAdmin)
admin.site.register(JobConnection,jobconnectionAdmin)

    



