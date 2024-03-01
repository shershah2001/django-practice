from django import forms 

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your Name",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label="Email Address",required=False,widget=forms.TextInput(attrs={'class':'form-control'}))