from django import forms

from .models import ProductModel



class ProductForm (forms.ModelForm):
    weight = forms.IntegerField(
        label = "Weight (gm)",
        widget = forms.NumberInput(attrs={'class':'form-control'})
        )
    class Meta:
        model = ProductModel
        fields = ['name','weight','price']
        labels = {'Name': 'name', 'Price': 'price'}
        
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}),
        
        'price':forms.NumberInput(attrs={'class':'form-control'})
        }