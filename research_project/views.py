from django.shortcuts import render
from .forms import GreetingForm


def index(request):
    greeting = "Welcome"
    if request.method == 'POST':
        form = GreetingForm(request.POST)
        if form.is_valid():
            greeting = form.cleaned_data['new_greeting']
            with open("greeting.txt", "w") as greet:
                greet.write(greeting)
    else:
        form = GreetingForm()
        with open("greeting.txt") as greet:
            greeting = greet.read()
    context = {'greeting': greeting, 'form': form}
    return render(request, 'research_project/index.html', context)
