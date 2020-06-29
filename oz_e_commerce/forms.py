from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label='Nome Completo', error_messages={'required': 'Obrigado buta seu nome'},
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Seu nome sua besta"
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        error_messages={'required': 'Email inválido'},
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email seu besta'
            }
        )
    )
    content = forms.CharField(
        label='Mensagem',
        error_messages={'required': 'É obrigatório o preenchimento do campo mensagem!'},
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mensagem não massagem'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'gmail.com' not in email:
            raise forms.ValidationError('O email deve ser do gmail.com')
        return email


class LoginForm(forms.Form):
    username = forms.CharField()

