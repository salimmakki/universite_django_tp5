from django import forms
from .models import Cours, Enseignant


class CoursForm(forms.ModelForm):
    class Meta:
        model = Cours
        fields = ['titre', 'description', 'credit', 'enseignant']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du cours'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Description'}),
            'credit': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'enseignant': forms.Select(attrs={'class': 'form-select'}),
        }


class EnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'specialite']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Spécialité'}),
        }
