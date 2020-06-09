from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(label='Nome Completo', error_messages={'required': 'Obrigado buta seu nome'},
                               widget=forms.TextInput(
                                   attrs={
                                       "class": "form-control",
                                       "placeholder": "Seu nome sua besta"
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
