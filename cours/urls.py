from django.urls import path
from . import views

urlpatterns = [
    # Accueil
    path('', views.accueil, name='accueil'),

    # Authentification
    path('connexion/', views.connexion_utilisateur, name='connexion'),
    path('deconnexion/', views.deconnexion_utilisateur, name='deconnexion'),

    # Cours
    path('cours/', views.liste_cours, name='liste_cours'),
    path('cours/ajouter/', views.ajouter_cours, name='ajouter_cours'),
    path('cours/modifier/<int:pk>/', views.modifier_cours, name='modifier_cours'),
    path('cours/supprimer/<int:pk>/', views.supprimer_cours, name='supprimer_cours'),

    # Enseignants
    path('enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('enseignants/modifier/<int:pk>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('enseignants/supprimer/<int:pk>/', views.supprimer_enseignant, name='supprimer_enseignant'),
]
