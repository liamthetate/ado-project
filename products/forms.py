from django import forms
from .models import Category, Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__' #dunder! makes it all fields
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_names()) for c in categories]

        self.fields['category'].choices = get_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'




