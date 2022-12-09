from django.db import models

class Ligue(models.Model):
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom
    def get_equipes(self):
        equipes = Equipe.objects.all().filter(ligue=self.ID)
        for equipe in equipes:
            matches= Match.objects.all().filter(locaux=equipe.ID) | Match.objects.all().filter(visiteur=equipe.ID)
            final = 0
            for results in matches :
                if results.visiteur.ID == equipe.ID:
                    print()
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
            equipe.point = final
            print(equipe.ID, ':' ,equipe.point)
        return equipes
            
    
class Equipe(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    point = models.IntegerField(default=0)
    def get_matches(self):
        matches= Match.objects.all().filter(locaux=self.ID) | Match.objects.all().filter(visiteur=self.ID)
        for results in matches :
            if results.visiteur.ID == self.ID:
                if results.score_visiteurs > results.score_locaux:
                    results.point_locaux = 0
                    results.point_visteur = 3
                elif results.score_visiteurs == results.score_locaux:
                    results.point_locaux = 1
                    results.point_visteur = 1
                else:
                    results.point_locaux = 3
                    results.point_visteur = 0
            else:
                if results.score_visiteurs < results.score_locaux:
                    results.point_locaux = 3
                    results.point_visteur = 0
                elif results.score_visiteurs == results.score_locaux:
                    results.point_locaux = 1
                    results.point_visteur = 1
                else:
                    results.point_locaux = 0
                    results.point_visteur = 3
        return matches
    def __str__(self):
        return self.nom
    def some(self):
        matches= Match.objects.all().filter(locaux=self.ID) | Match.objects.all().filter(visiteur=self.ID)
        final = 0
        for results in matches :
            if results.visiteur.ID == self.ID:
                if results.score_visiteurs > results.score_locaux:
                    results.point_locaux = 0
                    results.point_visteur = 3
                    final += 3
                elif results.score_visiteurs == results.score_locaux:
                    results.point_locaux = 1
                    results.point_visteur = 1
                    final += 1
                else:
                    results.point_locaux = 3
                    results.point_visteur = 0
                    final += 0
            else:
                if results.score_visiteurs < results.score_locaux:
                    results.point_locaux = 3
                    results.point_visteur = 0
                    final += 3
                elif results.score_visiteurs == results.score_locaux:
                    results.point_locaux = 1
                    results.point_visteur = 1
                    final += 1
                else:
                    results.point_locaux = 0
                    results.point_visteur = 3
                    final += 0
        self.point = final
        return final
    
    
class Match(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    visiteur = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name="visiteurs")
    locaux = models.ForeignKey(Equipe, on_delete=models.CASCADE, related_name="locaux")
    score_visiteurs = models.IntegerField(default=0)
    score_locaux = models.IntegerField(default=0)
    point_locaux = models.IntegerField(default=0)
    point_visteur = models.IntegerField(default=0)
    
    
