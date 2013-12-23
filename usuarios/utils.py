from django.contrib.auth import authenticate, login


def ingreso(request, username, password):
    output = {}
    output['status'] = False
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
