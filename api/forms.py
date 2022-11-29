from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
# custom forms
class MyCustomSignupForm(forms.ModelForm):
  name = forms.CharField(max_length=50)
  picture =  forms.FileField()
  
    
  def save(self, commit: bool = False):
    Profile.objects.create(name=self.name, picture = self.priture)
    return super().save(commit)
  
  class Meta:
    model = get_user_model()
    fields =['name','username',  'password']
    
    
    
class MyCustomLoginForm(forms.ModelForm):
  name = forms.CharField(max_length=50)
  picture =  forms.FileField()
  
    
  def save(self, commit: bool = False):
    Profile.objects.create(name=self.name, picture = self.priture)
    return super().save(commit)
  
  class Meta:
    model = get_user_model()
    fields =['name','username',  'password']
    
    
    
  