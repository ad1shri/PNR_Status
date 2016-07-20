from django import forms

class NameForm(forms.Form):
    pnrno = forms.CharField(label='Your PNR no.', max_length=10)