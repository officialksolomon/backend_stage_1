from django import forms
from django.contrib.auth import get_user_model
from .models import Profile
from allauth.account.forms import LoginForm, SignupForm
# custom forms
class MyCustomSignupForm(SignupForm):
  name = forms.CharField(max_length=50)
  picture =  forms.ImageField(required=False, allow_empty_file=True)
  
  
  class Meta:
    model = get_user_model()
    fields =['name','username',  'password']
    exclude =['name',]
    
    
    
class MyCustomLoginForm(LoginForm):
  name = forms.CharField(max_length=50)
  picture =   forms.ImageField(required=False)
  
    
  def save(self, commit: bool = False):
    Profile.objects.create(name=self.name, picture = self.picture, user = self.pk)
    return super().save(commit)
  
  class Meta:
    model = get_user_model()
    fields =['name','username',  'password']
    
    
    
  