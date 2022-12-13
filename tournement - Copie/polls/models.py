from django.db import models

class Ligue(models.Model):
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom
    def get_matches(self):
        matches= Match.objects.all().filter(ligue=self.ID).filter(score_visiteurs='-')
        return matches
    def get_equipes(self):
        equipes = Equipe.objects.all().filter(ligue=self.ID)
        for equipe in equipes:
            matches= Match.objects.all().filter(locaux=equipe.ID) | Match.objects.all().filter(visiteur=equipe.ID)
            final = 0
            for results in matches :
                if results.score_visiteurs != '-' and results.score_visiteurs != '-':
                    if results.visiteur.ID == equipe.ID:
                        if results.score_visiteurs > results.score_locaux:
                            final += 3
                        elif results.score_visiteurs == results.score_locaux and results.score_visiteurs != '-':
                            final += 1
                        else:
                            final += 0
                    else:
                        if results.score_visiteurs < results.score_locaux:
                            final += 3
                        elif results.score_visiteurs == results.score_locaux and results.score_visiteurs != '-':
                            final += 1
                        else:
                            final += 0
            equipe.point = final
            print(equipe.ID, ':' ,equipe.point)
            equipe.save()
        return equipes
            
    
class Equipe(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=50)
    point = models.IntegerField(default=0)
    def get_matches(self):
        matches= Match.objects.all().filter(locaux=self.ID) | Match.objects.all().filter(visiteur=self.ID)
        return matches
    def __str__(self):
        return self.nom
    def some(self):
        matches= Match.objects.all().filter(locaux=self.ID) | Match.objects.all().filter(visiteur=self.ID)
        final = 0
        for results in matches :
            if results.visiteur.ID == self.ID:
                if results.score_visiteurs > results.score_locaux:
                    final += 3
                elif results.score_visiteurs == results.score_locaux:
                    final += 1
                else:
                    final += 0
            else:
                if results.score_visiteurs < results.score_locaux:
                    final += 3
                elif results.score_visiteurs == results.score_locaux:
                    final += 1
                else:
                    final += 0
        self.point = final
        self.save()
        return final
    
    
class Match(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    visiteur = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name="visiteurs")
    locaux = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name="locaux")
    score_visiteurs = models.CharField(default='-', max_length=2)
    score_locaux = models.CharField(default='-',max_length=2)
    date = models.DateField()
    
    
