from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'placeholder': 'Digite seu nome de usuário'})
        self.fields['password1'].widget.attrs.update(
            {'placeholder': 'Digite sua senha'})
        self.fields['password2'].widget.attrs.update(
            {'placeholder': 'Confirme sua senha'})
        self.fields[
            'username'].help_text = 'Somente permitidos letras, números e caracteres especiais (@/./+/-/_)/'
        self.fields['password1'].help_text = 'A senha deve ter no minimo 8 caracteres e deve conter pelo menos um caracter especial.'
        self.fields['password2'].help_text = 'Confirme a senha.'
