from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.forms import ModelForm
from .forms import MatchForm

from .models import Ligue, Equipe, Match

def index(request):
    latest_ligue_list = Ligue.objects.all
    context = {'latest_ligue_list': latest_ligue_list}
    return render(request, 'polls/index.html', context)

def detail(request, ligue):
    ligue = get_object_or_404(Ligue, pk=ligue)
    return render(request, 'polls/detail.html', {'ligue': ligue})


def results(request, equipe):
    equipe = get_object_or_404(Equipe, pk=equipe)
    return render(request, 'polls/results.html', {'equipe': equipe})

def post(request, ligue):
    ligue = get_object_or_404(Ligue, pk=ligue)
    # if this is a POST request we need to process the form data
    form = MatchForm()
    context = {'form': form, 'ligue': ligue}
    return render(request, 'polls/post.html', context)

def match(request, match):
    match = get_object_or_404(Match, pk=match)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MatchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('mouhaha')
            post = form.save(commit=False)
            post.id = match.id
            post.ligue = match.ligue
            post.visiteur = match.visiteur
            post.locaux = match.locaux
            post.date = match.date
            post.save()
            url = "/polls/"+str(match.ligue.ID)+"/post"
            return HttpResponseRedirect(url)
        else :
            print('top')
    # if a GET or any other method) we'll create a blank form
    else:
        print('tozeeeeeeee')
        return HttpResponseRedirect('/polls')
