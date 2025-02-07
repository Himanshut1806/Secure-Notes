from django import forms
from django.contrib.auth.models import User
from social.models import Note

class UserRegistrationForm(forms.Form):
    Name1 = forms.CharField(max_length = 100, required = True )
    Username1 = forms.CharField(max_length = 100, required = True )
    Email1 = forms.EmailField(max_length = 100, required = True )
    Password1 = forms.CharField(max_length = 20, required = True,  )
    Confirmpassword1 = forms.CharField(max_length = 20, required = True )

class UserLoginForm(forms.ModelForm):
     class Meta:
        model = User
        fields="username", "password"


class NoteForm(forms.ModelForm):
    class Meta:
        model= Note
        fields = "title","description"