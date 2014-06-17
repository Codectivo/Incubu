# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.forms import UserCreateForm


class UsuariosRegistroTest(TestCase):
    """Test para el formulario de registro"""

    @classmethod
    def setUpClass(self):
        usu = User.objects.create_user(
            username='user_test',
            email='user@test.com',
            password='thistest')
        usu.save()

        self.form_data = {
            'username': 'user_test_1',
            'email': 'user_1@test.com',
            'password1': 'mipassword',
            'password2': 'mipassword'
        }

    def test_usuario(self):
        #Test usuario no repetir
        form_data = self.form_data.copy()
        form_data['username'] = "user_test"
        form = UserCreateForm(
            data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_email(self):
        #Test no repetir email
        form_data = self.form_data.copy()
        form_data['email'] = "user@test.com"
        form = UserCreateForm(
            data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_password(self):
        #Password no coinciden
        form_data = self.form_data.copy()
        form_data['password1'] = "u1234"
        form = UserCreateForm(
            data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_ok(self):
        #Test con data OK
        form_data = self.form_data.copy()
        form_data['username'] = 'user_test_2'
        form_data['email'] = 'user_2@test.com'
        form = UserCreateForm(
            data=form_data)
        self.assertEqual(form.is_valid(), True)
