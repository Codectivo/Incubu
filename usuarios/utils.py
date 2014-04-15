from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def ingreso(request, username, password):
    output = {}
    output['status'] = False
    if '@' in username:
        user = User.objects.get(email=username)
        username = user.username
    access = authenticate(username=username, password=password)
    if access:
        if not access.is_active:
            output['response'] = 'Cuenta desactivada.'
    else:
        output['response'] = 'Usuario o Clave incorrectos.'
    if 'response' not in output:
        login(request, access)
        output['status'] = True
    return output
