from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    """Formulario para crear y editar productos"""
    
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'stock', 'image', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción detallada del producto'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
        labels = {
            'name': 'Nombre del Producto',
            'description': 'Descripción',
            'category': 'Categoría',
            'price': 'Precio ($)',
            'stock': 'Stock',
            'image': 'Imagen del Producto',
            'is_active': 'Producto Activo'
        }

class CategoryForm(forms.ModelForm):
    """Formulario para crear y editar categorías"""
    
    class Meta:
        model = Category
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la categoría'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripción de la categoría'
            })
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción'
        }