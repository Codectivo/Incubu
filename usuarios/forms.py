from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Account


class UserCreateForm(UserCreationForm):
    """Form para creacion de Usuario"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(UserCreateForm, self).clean()
        cd = self.cleaned_data
        email = cd.get('email')
        username = cd.get('username')
        if email:
            try:
                us = User.objects.get(email=email)
                self._errors['email'] = "Email existente, escoger otro."
            except:
                pass
        if username:
            if '@' in username:
                self._errors['username'] = 'No se permite el @ en el Usuario'
        return cd


class AddAccount(forms.ModelForm):
    """Form para agregar ctas"""
    class Meta:
        model = Account
        fields = ("description", "user_account", "pass_account")


class UserEditForm(forms.ModelForm):
    """Custom Form para Configuracion de data del Usuario."""
    password_actual = forms.CharField(
        widget=forms.PasswordInput(), required=False)
    password = forms.CharField(
        widget=forms.PasswordInput(), required=False)
    repassword = forms.CharField(
        widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)

    def clean(self):
        super(UserEditForm, self).clean()
        cd = self.cleaned_data
        username = cd.get('username')
        password_actual = cd.get('password_actual')
        password = cd.get('password')
        repassword = cd.get('repassword')
        email = cd.get('email')
        if email and email != self.instance.email:
            try:
                us = User.objects.get(email=email)
                self._errors['email'] = "Email existente, escoger otro."
            except:
                pass
        if password_actual or password or repassword:
            if auth.authenticate(username=username, password=password_actual):
                if password and repassword:
                    if password != repassword:
                        self._errors['password'] = 'Los passwords nuevos no coinciden.'
                else:
                    self._errors['password'] = "Debe introducir ambos password."
            else:
                self._errors['password_actual'] = "El password actual no es correcto."
        return cd