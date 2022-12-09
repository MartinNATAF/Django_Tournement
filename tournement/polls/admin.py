from django.contrib import admin

from .models import Ligue, Equipe, Match

admin.site.register(Ligue)
admin.site.register(Equipe)
admin.site.register(Match)