


from django.forms import FileInput, ModelForm, TextInput, Textarea
from .models import property

class Property_Form(ModelForm):
    class Meta:
        model=property
        fields=['placename','location','image','acres','description']
        
        
        widgets = {

            'placename': TextInput(
                                    attrs={'class': 'form-control'}),
            'location': TextInput(
                attrs={'class': 'form-control'}) ,
            'image': FileInput(
                                    attrs={'class': 'form-control'}),
            'acres': TextInput(
                attrs={'class': 'form-control'}),
            'description': Textarea(
                attrs={'class': 'form-control'}),

        }