# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.forms import UserEditForm


class UsuariosFormTest(TestCase):
    """Test para el formulario de configuracion"""

    @classmethod
    def setUpClass(self):
        #Crear Usuario
        self._user = []
        for i in range(0, 2):
            usu = User.objects.create_user(
                username='user_test_{}'.format(i),
                email='user_{}@test.com'.format(i),
                password='thistest')
            usu.save()
            self._user.append(usu)

        self.form_data = {
            'username': 'user_test_1',
            'email': 'user_1@test.com',
            'password_actual': 'thistest',
            'password': 'mipassword',
            'repassword': 'mipassword'
        }

    def test_user(self):
        """Test no repetir user"""
        form_data = self.form_data.copy()
        form_data['username'] = 'user_test_1'
        form = UserEditForm(
            data=form_data,
            instance=self._user[0])
        self.assertEqual(form.is_valid(), False)

    def test_email(self):
        """Test no repetir email"""
        form_data = self.form_data.copy()
        form_data['email'] = 'user_1@test.com'
        form = UserEditForm(
            data=form_data,
            instance=self._user[0])
        self.assertEqual(form.is_valid(), False)

    def test_passwords(self):
        """Test password"""
        form_data = self.form_data.copy()
        #Password actual erroneo
        form_data['password_actual'] = 'err_password'
        form = UserEditForm(
            data=form_data,
            instance=self._user[0])
        self.assertEqual(form.is_valid(), False)

        # Password nuevos no coinciden
        form_data['password'] = 'err_password'
        form = UserEditForm(
            data=form_data,
            instance=self._user[0])
        self.assertEqual(form.is_valid(), False)

    def test_ok(self):
        """Testear con datos ok"""
        form_data = self.form_data.copy()
        form = UserEditForm(
            data=form_data,
            instance=self._user[1])
        print form.errors
        self.assertEqual(form.is_valid(), True)
