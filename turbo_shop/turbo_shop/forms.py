from django import  forms

#from django.contrib.auth.models import  User
from users.models import User

class RegistroForm(forms.Form):
    username = forms.CharField(required=True, min_length=4, max_length=40, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username',
        'placeholder':"Nombre de Usuario"
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id':'email',
        'placeholder':'Correo Electronico'
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'di': 'password',
        'placeholder': 'Contraseña'
    }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username = username).exists():
            raise forms.ValidationError("El username ya se encuentra en uso")

        return username
        pass
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("El correo ya se encuentra en uso")

        return email
        pass

pass

class LoginForm(forms.Form):
     username_login = forms.CharField(required=True, min_length=4, max_length=40, widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'username_login',
        'name':'username_login',
        'placeholder':"Nombre de Usuario"
    }))
     password_login = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'di': 'password_login',
        'name': 'password_login',
        'placeholder': 'Contraseña'
    })) 
pass