from django.contrib import admin
from .models import Salle, Classe, UE, Desiderata, EmploiDuTemps
from django.contrib import messages

@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):
    list_display = ('ue', 'salle', 'jour', 'plage_horaire', 'date_passage')
    
    # Message d'alerte quand une programmation est ajoutée
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        messages.success(request, "Alerte : Un créneau a été ajouté à l'emploi du temps.")

admin.site.register(Salle)
admin.site.register(Classe)
admin.site.register(UE)
admin.site.register(Desiderata)