from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    feature1.number = "12%"
    feature1.mode = "increase"
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'hight'
    feature2.details = 'see futear'
    feature2.number = "6.5%"
    feature2.mode = "decrease"
    feature2.is_true = False

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'ultra'
    feature3.details = 'over the level'
    feature3.number = "23.6%"
    feature3.mode = "increase"
    feature3.is_true = True

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features': features})


def counter(request):
    # we experinced just ok with text name in index and here
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})
