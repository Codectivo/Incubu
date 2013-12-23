from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import Account


class UserCreateForm(UserCreationForm):
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
        if email:
            try:
                us = User.objects.get(email=email)
                self._errors['email'] = "Email existente, escoger otro."
            except:
                pass
        return cd
            


class AddAccount(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("description", "user_account", "pass_account")
