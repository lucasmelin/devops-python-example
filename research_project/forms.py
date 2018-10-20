from django import forms


class GreetingForm(forms.Form):
    new_greeting = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-small is-primary'}),
                                   label='New Greeting', max_length=100)
