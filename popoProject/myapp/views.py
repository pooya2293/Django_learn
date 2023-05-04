from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'hight'
    feature2.details = 'see futear'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'ultra'
    feature3.details = 'over the level'

    return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2, 'feature3': feature3})


def counter(request):
    # we experinced just ok with text name in index and here
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
