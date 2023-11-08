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

    def clean(self):
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )        
        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()