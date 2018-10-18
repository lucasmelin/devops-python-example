from django import forms


class GreetingForm(forms.Form):
    new_greeting = forms.CharField(label='New Greeting', max_length=100)
