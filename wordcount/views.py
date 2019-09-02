from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html', {'name':'khalid btb'})

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1
    
    sorteddictionary = sorted(worddictionary.items(), key=operator.itemgetter(1),reverse=True)

    return render(request, 'count.html',{'sorteddictionary':sorteddictionary,'wordlist':wordlist,'fulltext':fulltext,'count':len(wordlist)})


def quiz(request):
    return render(request,'quiz.html')

def resultat(request):
    note=0
    result = request.GET['question1']
    if result =='Oui':
        note=100
    else:
        note=0
    return render(request,'results.html',{'note':note})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')