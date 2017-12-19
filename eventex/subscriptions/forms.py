from django import forms

from eventex.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email')
    phone = forms.CharField(label='Telefone')

    def clean_name(self):
        name = self.cleaned_data['name']
        words = []
        for w in name.split():
            if len(w) > 2:
                words.append(w.capitalize())
            else:
                words.append(w)

        return ' '.join(words)
