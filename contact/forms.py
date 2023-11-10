from django import forms
from django.core.exceptions import ValidationError
from . import models



class ContactForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu primeiro nome'}),
                                 label='Nome', help_text='Texto de ajuda para o usuário')
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu sobrenome'}),
                                 label='Sobrenome', help_text='Texto de ajuda para o usuário')    
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escreva seu número de telefone'}),
                                 label='Telefone', help_text='Texto de ajuda para o usuário')

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',)


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