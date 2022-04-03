from django import forms

#from attr import attrs
#from matplotlib import widgets
from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweetTitle', 'tweetTitleTag', 'tweetAuthor', 'tweetText')


        widgets = {
            'tweetTitle': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Choose your title'}),
            'tweetTitleTag': forms.TextInput(attrs = {'class':'form-control'}),
            'tweetAuthor': forms.Select(attrs = {'class':'form-control'}),
            'tweetText': forms.Textarea(attrs = {'class':'form-control'}),


        }


class EditTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweetTitle', 'tweetTitleTag', 'tweetText')


        widgets = {
            'tweetTitle': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Choose your title'}),
            'tweetTitleTag': forms.TextInput(attrs = {'class':'form-control'}),
            #'tweetAuthor': forms.Select(attrs = {'class':'form-control'}),
            'tweetText': forms.Textarea(attrs = {'class':'form-control'}),


        }