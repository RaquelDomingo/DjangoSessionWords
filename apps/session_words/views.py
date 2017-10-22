from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request, 'session_words/index.html')

def add_word(request):
    try:
        font = request.POST['bigFont']
    except KeyError:
        font = "small"
    
    if request.method == "POST":

        words = {
            "word": request.POST['word'],
            "color": request.POST['color'],
            "font": font,
            "time": strftime('%H:%M:%S %p, %B %d %Y', gmtime())
        }
    
    wordsList = []
    wordsList.append(words)
    try:
        request.session['history'] += wordsList
    except KeyError:
        request.session['history'] = wordsList
    print request.session['history']
    return redirect('/')

def clear(request):
    request.session['history'] = []
    print request.session['history']
    return redirect('/')