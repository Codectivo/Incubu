import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from usuarios.forms import UserCreateForm, AddAccount, UserEditForm
from usuarios.models import Account


def registra(request):
    output = {}
    if request.method == 'POST':
        form_reg = UserCreateForm(data=request.POST)
        if form_reg.is_valid():
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password1')
            userDB = User.objects.create_user(username, email, password)
            userDB.save()
            access = authenticate(username=username, password=password)
            login(request, access)
            return HttpResponseRedirect('/usuario/escritorio/')
        else:
            output['errors'] = 'Ha ocurrido un error favor de revisar el formulario'
    else:
        form_reg = UserCreateForm()
    output['usuario_registra'] = form_reg
    return render(request, "usuarios/registra.html", output)


@login_required
def escritorio(request):
    output = {}
    output['accounts'] = Account.objects.filter(user=request.user)
    output['add_account'] = AddAccount()
    return render(request, "usuarios/escritorio.html", output)


@login_required
def logouts(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required
def add_key(request):
    response = {}
    if request.is_ajax() and request.method == 'POST':
        description = request.POST.get('description')
        user_account = request.POST.get('user_account')
        pass_account = request.POST.get('pass_account')
        try:
            acc = Account(
                description=description,
                user_account=user_account,
                pass_account=pass_account,
                user=request.user)
            acc.save()
            response['estatus'] = True
        except Exception, e:
            response['estatus'] = False
            response['errors'] = e
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(status=400)


@login_required
def edit_key(request):
    response = {}
    if request.is_ajax() and request.method == 'POST':
        description = request.POST.get('description')
        user_account = request.POST.get('user_account')
        pass_account = request.POST.get('pass_account')
        account_id = request.POST.get('account_id')
        try:
            acc = Account.objects.get(pk=account_id)
            acc.description = description
            acc.user_account = user_account
            acc.pass_account = pass_account
            acc.save()
            response['estatus'] = True
        except Exception, e:
            response['estatus'] = False
            response['errors'] = e
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(status=400)


@login_required
def delete_key(request):
    response = {}
    if request.is_ajax() and request.method == 'POST':
        data_id = request.POST.get('data_id')
        try:
            acc = Account.objects.get(id=data_id).delete()
            response['estatus'] = True
        except Exception, e:
            response['estatus'] = False
            response['errors'] = e
        return HttpResponse(json.dumps(response))
    else:
        return HttpResponse(status=400)


@login_required
def configuracion(request):
    output = {}
    output['estatus'] = False
    if request.method == "POST":
        user_edit = UserEditForm(request.POST, instance=request.user)
        if user_edit.is_valid():
            password_actual = request.POST.get('password_actual')
            password = request.POST.get('password')
            repassword = request.POST.get('repassword')
            user_edit.save()
            if password_actual and password and repassword:
                request.user.set_password(password)
                request.user.save()
            output['estatus'] = True
    else:
        user_edit = UserEditForm(instance=request.user)
    output['user_edit_form'] = user_edit
    return render(request, "usuarios/configuracion.html", output)
