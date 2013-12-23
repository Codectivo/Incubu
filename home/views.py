# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from usuarios.utils import ingreso


def home(request):
    output = {}
    if request.method == 'POST':
        form_auth = AuthenticationForm(request.POST)
        if form_auth.is_valid:
            username = request.POST.get('username')
            password = request.POST.get('password')
            ing = ingreso(request, username, password)
            if ing['status']:
                return HttpResponseRedirect('/usuario/escritorio/')
            else:
                output['error_usuario_login'] = ing['response']
    else:
        form_auth = AuthenticationForm()
    output['usuario_login'] = form_auth
    return render(request, "home/index.html", output)
