from django import forms

class CharlaForm(forms.Form):
    nombre = forms.CharField()
    titulo = forms.CharField()
    email = forms.EmailField()
    resumen = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CharlaForm, self).__init__(*args, **kwargs)
        #Add html class to fields
        self.fields['nombre'].widget.attrs['class'] = 'u-full-width'
        self.fields['titulo'].widget.attrs['class'] = 'u-half-width'
        self.fields['email'].widget.attrs['class'] = 'u-full-width'
        self.fields['resumen'].widget.attrs['class'] = 'u-full-width'

class ContactoForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required =False)
    mensaje = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        #Add html class to fields
        self.fields['nombre'].widget.attrs['class'] = 'u-full-width'
        self.fields['website'].widget.attrs['class'] = 'u-half-width'
        self.fields['email'].widget.attrs['class'] = 'u-full-width'
        self.fields['mensaje'].widget.attrs['class'] = 'u-full-width'
