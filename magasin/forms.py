# magasin/forms.py
from django.forms import ModelForm
from .models import Produit, Fournisseur

class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"

class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = "__all__"
