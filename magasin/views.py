# magasin/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.template import loader
from .models import Produit, Fournisseur
from .forms import ProduitForm, FournisseurForm

def index(request):
    if request.method == "POST":
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = ProduitForm()  # créer formulaire vide

    list = Produit.objects.all()
    return render(request, 'magasin/base.html', {'list': list, 'form': form})

def nouveauFournisseur(request):
    if request.method == "POST":
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FournisseurForm()

    fournisseurs = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'form': form, 'fournisseurs': fournisseurs})
