from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ContactForm(forms.ModelForm):

    # first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu primeiro nome'}),
    #                              label='Nome', help_text='Texto de ajuda para o usuário')
    
    # last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu sobrenome'}),
    #                              label='Sobrenome')    
    # phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu número de telefone'}),
    #                              label='Telefone')
    # email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Escreva o email do contato'}),
    #                              label='Email')
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={'accept': 'image/*'}))

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',)


    # Valor de mais de um campo
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error('last_name', ValidationError('O segundo nome não pode ser igual ao primeiro', code='invalid'))
       

        return super().clean()
    
    # Valor de apenas um campo
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
             self.add_error('first_name', ValidationError('Mensagem de erro', code='invalid'))   

        return first_name

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email existente', code='invalid')
            )

        return email