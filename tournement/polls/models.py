from django.db import models

class Ligue(models.Model):
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom
    
class Equipe(models.Model):
    ligue = models.ForeignKey(Ligue, on_delete=models.CASCADE)
    ID = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom
    # joueurs: Participant[]
