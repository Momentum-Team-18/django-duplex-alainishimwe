from django.shortcuts import render, redirect, get_object_or_404
from .models import Card
from .forms import CardForm
import random

# Create your views here.
# def home(request):

#     return render(request, 'flashCards/index.html')

def card(request):
    cards = Card.objects.all()
    return render(request, 'flashCards/index.html', {'cards': cards})

def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save()
            card.save()
            return redirect('card')
    else:
        form = CardForm()
    return render(request, 'flashCards/addCard.html', {'form': form})

def show_answer(request,pk):
    card = get_object_or_404(Card, pk=pk)

    return render(request, 'flashCards/answer.html', {'card': card})

def random_card(request):
    max_pk = Card.objects.values('id').order_by("-id")[0]
    pk = random.randint(1, max_pk['id'])
    card = Card.objects.get(pk=pk)

    return render(request, 'flashCards/randomCard.html', {'card':card})
