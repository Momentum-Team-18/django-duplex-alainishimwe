from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Card
from .forms import CardForm
import random

# Create your views here.
def home(request):

    return render(request, 'flashCards/home.html')

# @login_required(login_url='home')
def card(request):
    cards = Card.objects.all()
    return render(request, 'flashCards/index.html', {'cards': cards})

@login_required(login_url='home')
def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect('card')
    else:
        form = CardForm()
    return render(request, 'flashCards/addCard.html', {'form': form})

@login_required(login_url='home')
def show_answer(request,pk):
    card = get_object_or_404(Card, pk=pk)

    return render(request, 'flashCards/answer.html', {'card': card})

@login_required(login_url='home')
def random_card(request):
    max_pk = Card.objects.values('id').order_by("-id")[0]
    pk = random.randint(1, max_pk['id'])
    card = Card.objects.get(pk=pk)

    return render(request, 'flashCards/randomCard.html', {'card':card})
