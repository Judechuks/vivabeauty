from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# CustomerRegistration form
class CustomerRegistrationForm(UserCreationForm):
  username = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={
      'autofocus': 'True',
      'placeholder': 'Username *',
      'class': 'form-control',
    })
  )
  email = forms.EmailField(
    widget=forms.EmailInput(attrs={
      'placeholder': 'Email *',
      'class': 'form-control',
    })
  )
  password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={
      'placeholder': 'Password *',
      'class': 'form-control',
    })
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={
      'placeholder': 'Confirm Password *',
      'class': 'form-control',
    })
  )

  class Meta:
    model = User # User model from django
    fields = ['username', 'email', 'password1', 'password2'] # fields to display

  # making sure already used/picked email can't be used for registration
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if User.objects.filter(email=email).exists():
      raise forms.ValidationError('This email address is already registered.')
    return email