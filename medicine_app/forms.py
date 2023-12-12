from django import forms


# class NameForm(forms.Form):
#     Search = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':70}))


class NameForm1(forms.Form):
    Message     = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':70}))
    NumbertoCall = forms.CharField(label="NumbertoCall")  


# class NameForm1(forms.Form):
#     Message     = forms.CharField(label="Message", max_length=100)
#     NumbertoCall = forms.CharField(label="NumbertoCall")   


#from django import forms


# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)
