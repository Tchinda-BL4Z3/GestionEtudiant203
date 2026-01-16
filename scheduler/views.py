from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Salle, Classe, UE, EmploiDuTemps
from django.contrib.auth.models import User

# --- 1. PAGES PUBLIQUES ---
def home_view(request):
    return render(request, 'scheduler/dashboard.html')

def login_view(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        role_selectionne = request.POST.get('role')
        user = authenticate(username=u, password=p)
        
        if user is not None:
            login(request, user)
            if role_selectionne == 'admin':
                return redirect('admin_dashboard')
            return redirect('home')
        else:
            messages.error(request, "Identifiant ou mot de passe incorrect.")
    return render(request, 'scheduler/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# --- 2. CONSOLE ADMIN ---
@login_required
def admin_dashboard(request):
    context = {
        'total_salles': Salle.objects.count(),
        'total_profs': User.objects.filter(is_staff=False).count(),
        'total_classes': Classe.objects.count(),
        'total_ue': UE.objects.count(),
    }
    return render(request, 'scheduler/adminConsole.html', context)

# --- 3. GESTION DES RESSOURCES ---
@login_required
def admin_salles(request):
    if request.method == "POST":
        Salle.objects.create(
            nom=request.POST.get('nom'),
            capacite=request.POST.get('capacite'),
            type_salle=request.POST.get('type')
        )
        return redirect('admin_salles')
    return render(request, 'scheduler/adminSalle.html', {'salles': Salle.objects.all()})

@login_required
def admin_classes(request):
    if request.method == "POST":
        Classe.objects.create(
            nom=request.POST.get('nom'),
            filiere=request.POST.get('filiere'),
            effectif=request.POST.get('effectif'),
            departement=request.POST.get('departement')
        )
        return redirect('admin_classes')
    classes = Classe.objects.all()
    total_etudiants = sum(c.effectif for c in classes)
    return render(request, 'scheduler/adminClasse.html', {'classes': classes, 'total_etudiants': total_etudiants})

@login_required
def admin_ue(request):
    if request.method == "POST":
        classe_id = request.POST.get('classe_id')
        if classe_id:
            classe_obj = get_object_or_404(Classe, id=classe_id)
            UE.objects.create(code=request.POST.get('code'), nom=request.POST.get('nom'), classe=classe_obj)
        return redirect('admin_ue')
    return render(request, 'scheduler/adminUE.html', {'ues': UE.objects.all(), 'classes': Classe.objects.all()})

# --- 4. LES FONCTIONS DE SUPPRESSION (Pour corriger tes erreurs d'URL) ---

# Fonction spécifique demandée à la ligne 34 de ton urls.py
@login_required
def delete_salle(request, id):
    get_object_or_404(Salle, id=id).delete()
    return redirect('admin_salles')

# Fonction spécifique pour les classes
@login_required
def delete_classe(request, id):
    get_object_or_404(Classe, id=id).delete()
    return redirect('admin_classes')

# Fonction spécifique pour les UE (le message d'erreur te l'a suggérée)
@login_required
def delete_ue(request, id):
    get_object_or_404(UE, id=id).delete()
    return redirect('admin_ue')

# Fonction GÉNÉRIQUE demandée à la ligne 38 de ton urls.py
@login_required
def delete_item(request, model_type, id):
    if model_type == 'salle':
        get_object_or_404(Salle, id=id).delete()
    elif model_type == 'classe':
        get_object_or_404(Classe, id=id).delete()
    elif model_type == 'ue':
        get_object_or_404(UE, id=id).delete()
    return redirect(request.META.get('HTTP_REFERER', 'admin_dashboard'))

# Extrait de views.py pour admin_dashboard
@login_required
def admin_dashboard(request):
    if request.method == "POST":
        action = request.POST.get('action')
        if action == "add_salle":
            Salle.objects.create(
                nom=request.POST.get('nom'),
                capacite=request.POST.get('capacite'),
                type_salle=request.POST.get('type') # Assure-toi que le name est 'type' dans le HTML
            )
        elif action == "add_classe":
            Classe.objects.create(
                nom=request.POST.get('nom'),
                filiere=request.POST.get('filiere'),
                effectif=request.POST.get('effectif')
            )
        return redirect('admin_dashboard')

    context = {
        'total_salles': Salle.objects.count(),
        'total_profs': User.objects.count(), # Compte tous les utilisateurs
        'total_classes': Classe.objects.count(),
        'total_ue': UE.objects.count(),
    }
    return render(request, 'scheduler/adminConsole.html', context)