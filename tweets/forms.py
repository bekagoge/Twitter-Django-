from django import forms

#from attr import attrs
#from matplotlib import widgets
from .models import Tweet, Category




choices = Category.objects.all().values_list('name','name')
#^^^variable for choice category for tweets
choice_list = []
for item in choices:
    choice_list.append(item)
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('tweetTitle', 'tweetTitleTag', 'tweetAuthor', 'tweetCategory', 'tweetText')

        widgets = {
            'tweetTitle': forms.TextInput(attrs = {'class':'form-control', 'placeholder': 'Choose your title'}),
            'tweetTitleTag': forms.TextInput(attrs = {'class':'form-control'}),
            'tweetAuthor': forms.Select(attrs = {'class':'form-control'}),
            'tweetCategory': forms.Select(choices = choice_list, attrs = { 'class':'form-control'}),
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