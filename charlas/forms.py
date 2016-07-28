from django import forms

class CharlaForm(forms.Form):
    nombre = forms.CharField()
    titulo = forms.CharField()
    email = forms.EmailField()
    resumen = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CharlaForm, self).__init__(*args, **kwargs)
        #Add html class to fields
        self.fields['resumen'].widget.attrs['class'] = 'materialize-textarea'

class ContactoForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    website = forms.URLField(required =False)
    mensaje = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        #Add html class to fields
        self.fields['mensaje'].widget.attrs['class'] = 'materialize-textarea'
