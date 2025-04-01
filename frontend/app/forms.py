from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Producto')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripción', required=False)
    cantidad_disponible = forms.IntegerField(min_value=0, label='Cantidad Disponible')
    precio_unitario = forms.FloatField(min_value=0, label='Precio Unitario')
    categoria = forms.CharField(max_length=50, label='Categoría')