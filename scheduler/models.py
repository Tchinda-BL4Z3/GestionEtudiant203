from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Salle(models.Model):
    TYPES = [('Amphi', 'Amphi'), ('TD', 'TD'), ('Labo', 'Labo')]
    nom = models.CharField(max_length=50)
    capacite = models.IntegerField()
    type_salle = models.CharField(max_length=20, choices=TYPES, default='TD')

    def __str__(self):
        return f"{self.nom} ({self.capacite} places)"

class Classe(models.Model):
    nom = models.CharField(max_length=50) # Ex: ICT-L2
    filiere = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    effectif = models.IntegerField()

    def __str__(self):
        return self.nom

class UE(models.Model):
    code = models.CharField(max_length=10)
    nom = models.CharField(max_length=100)
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code} - {self.nom}"

class Desiderata(models.Model):
    enseignant = models.ForeignKey(User, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20, choices=[
        ('Lundi', 'Lundi'), ('Mardi', 'Mardi'), ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'), ('Vendredi', 'Vendredi'), ('Samedi', 'Samedi')
    ])
    plage_horaire = models.CharField(max_length=50) # Ex: 08h-10h
    valide = models.BooleanField(default=False) # Arbitrage Admin

    def __str__(self):
        return f"Vœu de {self.enseignant.username} - {self.jour}"

class EmploiDuTemps(models.Model):
    ue = models.ForeignKey(UE, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    jour = models.CharField(max_length=20)
    plage_horaire = models.CharField(max_length=50)
    date_passage = models.DateField()
    semestre = models.IntegerField(default=1)
    annee_academique = models.CharField(max_length=20, default="2025/2026")

    def clean(self):
        # Logique de programmation optimale : Vérifier capacité salle
        if self.salle.capacite < self.ue.classe.effectif:
            raise ValidationError(f"Capacité insuffisante ! La salle a {self.salle.capacite} places mais la classe a {self.ue.classe.effectif} étudiants.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)