from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from .models import Customer

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
  
# Login Form
class LoginForm(AuthenticationForm):
  username = UsernameField(widget=forms.TextInput(attrs={
    'autofocus': 'True', 
    'placeholder': 'Username *', 
    'class': 'form-control'
    })
  )
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'autocomplete': 'current-password *', 
    'placeholder': 'Password *', 
    'class': 'form-control'
    })
  )

# Customer's profile Form
class CustomerProfileForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['full_name', 'country', 'state', 'city', 'zipcode', 'phone_number', 'address']
    widgets = {
      'full_name': forms.TextInput(attrs={'autofocus': 'True', 'class': 'form-control'}),
      'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'+234**********', 'pattern':'+[0-9]{11,}', 'title':'NUMBERS ONLY AND SHOULD NOT BE LESS THAN 11 DIGITS'}),
      'country': forms.Select(attrs={'class': 'form-control'}),
      'state': forms.TextInput(attrs={'class': 'form-control'}),
      'city': forms.TextInput(attrs={'class': 'form-control'}),
      'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
      'address': forms.TextInput(attrs={'class': 'form-control'}),
    }

# Customer's Password Change Form - for customers to change their password if need be
class CustomerPasswordChangeForm(PasswordChangeForm):
  # inheriting the PasswordChangeForm from django
  old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus': 'True', 'placeholder': 'Enter your old password', 'class': 'form-control'}))
  new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password', 'class': 'form-control'}))
  new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password again', 'class': 'form-control'}))

# Customer's Password Reset Form - for customers to reset their password if forgotten
class CustomerPasswordResetForm(PasswordResetForm):
  # inheriting the PasswordResetForm from django
  email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': 'True', 'placeholder': 'Enter Email', 'class': 'form-control'}))

# Customer's Set Password Form - for customers to enter new password
class CustomerSetPasswordForm(SetPasswordForm):
  # inheriting the SetPasswordForm from django
  new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus': 'True', 'placeholder': 'Enter a new password', 'class': 'form-control'}))
  new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter new password again', 'class': 'form-control'}))