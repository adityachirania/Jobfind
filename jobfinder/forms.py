# importing what is necessary 
from django import forms
from .models import Job

class NewJobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('Type','Descripton','ApplyBy','Characteristics')
        

