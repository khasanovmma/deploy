from django import forms


class FeedBack(forms.Form):
    name = forms.CharField(max_length=150, label='',
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Ismingizni kiriting...', 'class': 'contact__input'}))
    email = forms.EmailField(max_length=150, label='', widget=forms.TextInput(
        attrs={'placeholder': 'Emailni kiriting...', 'class': 'contact__input'}))
    desc = forms.CharField(label='', widget=forms.Textarea(
        attrs={'placeholder': 'Matin kiriting...', 'class': 'contact__textarea'}))
