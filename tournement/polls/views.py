from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import MatchForm
import datetime, random, http.client, json

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
    
    
def create_match(request, ligue):
    ligue = get_object_or_404(Ligue, pk=ligue)
    for equipe in ligue.get_equipes():
        for equipe2 in ligue.get_equipes().exclude(ID=equipe.ID):
            try :
                matchtest = Match.objects.get(locaux = equipe.ID , visiteur = equipe2.ID)
            except ObjectDoesNotExist:
                match_enregistre = Match(
                    ligue=ligue,
                    locaux=equipe,
                    visiteur=equipe2,
                    date=datetime.date.today()
                                        )
                match_enregistre.save()
                try :
                    matchtest2 = Match.objects.get(locaux = equipe2.ID , visiteur = equipe.ID)
                except ObjectDoesNotExist:
                    match_enregistre = Match(
                        ligue=ligue,
                        locaux=equipe2,
                        visiteur=equipe,
                        date=datetime.date.today()
                                        )
                    match_enregistre.save()
    print(request,'lollll')
    url = "/polls/"+str(ligue.ID)
    return HttpResponseRedirect(url)
            
def ligue_random(request):
    r1 = random.randint(65,90)
    print(r1)
    url = "/polls/"
    conn = http.client.HTTPSConnection("livescore6.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "1e65f055e6msh5c1636eca4dcbc5p122054jsn56651182299b",
        'X-RapidAPI-Host': "livescore6.p.rapidapi.com"
        }

    conn.request("GET", "/competitions/get-table?CompId="+str(r1) , headers=headers)

    res = conn.getresponse()
    data = res.read()
    decode = json.loads(data)
    Stages = decode["Stages"]
    stage = Stages[0]
    league = stage["Snm"]
    country = stage["Cnm"]
    nom = league + ' ' + country
    ligue_enregistre = Ligue(
        ID=r1,
        nom=nom
    )
    ligue_enregistre.save()
    ligueT = get_object_or_404(Ligue, pk=r1)
    LiTab = stage["LeagueTable"]
    LT= LiTab["L"]
    Teams = LT[0]["Tables"][0]["team"]
    for i in range(len(Teams)):
        equipe_enregistre = Equipe(
            ligue=ligueT,
            nom=Teams[i]["Tnm"]
        )
        equipe_enregistre.save()
        print(Teams[i]["Tnm"])
    
    return HttpResponseRedirect(url)
                
