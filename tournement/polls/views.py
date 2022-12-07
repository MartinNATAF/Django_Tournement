from django.shortcuts import get_object_or_404, render

from .models import Equipe, Ligue

def index(request):
    latest_ligue_list = Ligue.objects.all
    context = {'latest_ligue_list': latest_ligue_list}
    return render(request, 'polls/index.html', context)

def detail(request, ligue):
    ligue = get_object_or_404(Ligue, pk=ligue)
    return render(request, 'polls/detail.html', {'ligue': ligue})