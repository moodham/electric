from django import forms


class commentform(forms.Form):
    name = forms.CharField(label='نام', max_length=100)
    message = forms.CharField(label='نظر',max_length=200)
    sender = forms.EmailField(label='ایمیل')

