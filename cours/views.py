from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Cours, Enseignant
from .forms import CoursForm, EnseignantForm


# ─── Authentification ─────────────────────────────────────────────────────────

def connexion_utilisateur(request):
    message = ""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('accueil')
        else:
            message = "Nom d'utilisateur ou mot de passe incorrect."
    return render(request, 'cours/connexion.html', {'message': message})


def deconnexion_utilisateur(request):
    logout(request)
    return redirect('connexion')


# ─── Accueil ──────────────────────────────────────────────────────────────────

def accueil(request):
    nb_cours = Cours.objects.count()
    nb_enseignants = Enseignant.objects.count()
    return render(request, 'cours/accueil.html', {
        'nb_cours': nb_cours,
        'nb_enseignants': nb_enseignants,
    })


# ─── CRUD Cours ───────────────────────────────────────────────────────────────

@login_required
def liste_cours(request):
    cours = Cours.objects.select_related('enseignant').all()
    return render(request, 'cours/liste_cours.html', {'cours': cours})


@login_required
def ajouter_cours(request):
    form = CoursForm()
    if request.method == 'POST':
        form = CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    return render(request, 'cours/ajouter_cours.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_cours(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    form = CoursForm(instance=cours)
    if request.method == 'POST':
        form = CoursForm(request.POST, instance=cours)
        if form.is_valid():
            form.save()
            return redirect('liste_cours')
    return render(request, 'cours/ajouter_cours.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_cours(request, pk):
    cours = get_object_or_404(Cours, pk=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('liste_cours')
    return render(request, 'cours/confirmer_suppression.html', {'objet': cours, 'type': 'cours'})


# ─── CRUD Enseignant ──────────────────────────────────────────────────────────

@login_required
def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'cours/liste_enseignants.html', {'enseignants': enseignants})


@login_required
def ajouter_enseignant(request):
    form = EnseignantForm()
    if request.method == 'POST':
        form = EnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    return render(request, 'cours/ajouter_enseignant.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    form = EnseignantForm(instance=enseignant)
    if request.method == 'POST':
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    return render(request, 'cours/ajouter_enseignant.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_enseignant(request, pk):
    enseignant = get_object_or_404(Enseignant, pk=pk)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('liste_enseignants')
    return render(request, 'cours/confirmer_suppression.html', {'objet': enseignant, 'type': 'enseignant'})
