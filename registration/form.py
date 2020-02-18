from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from datetime import date, datetime, timedelta
from django.utils import timezone

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email')

    class Meta :
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nama Depan'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Nama Belakang'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Konfirmasi Password'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input100'
            if visible.field.help_text :
                 visible.field.widget.attrs.update({'class':'input100 has-popover', 'data-content':visible.field.help_text, 'data-placement':'bottom', 'data-container':'body'})

    # def clean_email(self):
    #     # Get the email
    #     email = self.cleaned_data.get('email')

    #     # Check to see if any users already exist with this email as a username.
    #     try:
    #         match = User.objects.get(email=email)
            
    #     except User.DoesNotExist:
    #     # Unable to find a user, this is fine
    #         return email

    #     # A user was found with this as a username, raise an error.
    #     raise forms.ValidationError('This email address is already in use.')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Alamat Email Sudah Dipakai")
            print("This Email is Already Used")
        return email
    
    def clean_password2(self):
        password = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password Harus sama")
        return password


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

    username.widget.attrs['class'] = 'input100'
    password.widget.attrs['class'] = 'input100'

    username.widget.attrs['placeholder'] = 'Username'
    password.widget.attrs['placeholder'] = 'Password'

class UpdateUserForm(forms.ModelForm):
    class Meta :
        model = User
        fields = [
            'username', 
            'first_name',
            'last_name',
            'email',
        ]
    
    def clean_email(self):
        super().clean()
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

class ChangeUserPassword(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password Lama'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password Baru'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Konfirmasi Password Baru'}))

    def clean(self):
        super(ChangeUserPassword, self).clean()
        clean_new_password1 = self.cleaned_data.get('new_password1')
        clean_new_password2 = self.cleaned_data.get('new_password2')
        if clean_new_password1 and clean_new_password2:
            if clean_new_password1 != clean_new_password2 :
                raise forms.ValidationError("Password baru tidak sama")
        print(cleaned_data)
        return cleaned_data

# class DateInput(forms.DateInput):
#     input_type = 'date' 

class UpdateProfileForm(forms.ModelForm):
    bio = forms.CharField(max_length=500 , widget=forms.Textarea, required=False)
    profession = forms.CharField(max_length=100, label="Profesi", required=False)
    institute = forms.CharField(max_length=100, label="Instansi", required=False)
    birth_date = forms.DateField(label="Tanggal Lahir", required=False)
    phone_number = forms.CharField(max_length=20, label="Nomor Telepon", required=False)
    image_profile = forms.ImageField(required=False, label="Foto Profil")

    class Meta:
        model = Profile
        exclude = ['user', 'address']
        # widgets = {
        #     'birth_date': DateInput()
        # }

    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name != 'image_profile':
                visible.field.widget.attrs['class'] = 'form-control'
            # if visible.field.help_text :
            #      visible.field.widget.attrs.update({'class':'input100 has-popover', 'data-content':visible.field.help_text, 'data-placement':'bottom', 'data-container':'body'})