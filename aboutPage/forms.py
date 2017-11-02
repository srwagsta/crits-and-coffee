from django import forms


# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Name'}))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    contact_subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'message', 'rows': '25', 'cols': '10', 'placeholder': '  Message Text...'}))
