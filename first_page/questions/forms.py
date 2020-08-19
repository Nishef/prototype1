from django import forms
from . import models

#why do we need this?
#for validating forms
class QuestionForm(forms.ModelForm):
    #this is why we need meta:cause we want to validate some optional parts in models.py 
    class Meta:
        model = models.Question
        fields = ['title','description']
        
    #after that we use this class in views.py for validating