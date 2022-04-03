#from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.http import HttpResponse, Http404
from .models import Tweet
from .forms import TweetForm, EditTweetForm
from django.urls import reverse_lazy

# Create your views here.


#def homepage(request):
    #return render(request, 'homepage.html', {})


class HomePage(ListView):
    model = Tweet
    template_name = 'homepage.html'
    ordering = ['-tweetDate']
    #ordering = ['-id']

#^^^homepage view, puts tweets on main page

class PostDetailView(DetailView):
    model = Tweet
    template_name = 'postDetails.html'

#^^^tweets view, puts one tweet on page


class AddTweetView(CreateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'postingPage.html'
    #fields = '__all__'
    #fields = ('tweetTitle', tweetTitleTag', 'tweetAuthor', 'tweetText')

#^^^ create posting tweets on out oage

class UpdateTweetView(UpdateView):
    model = Tweet
    form_class = EditTweetForm
    template_name = 'update_tweet.html'
    #fields = ['tweetTitle', 'tweetTitleTag', 'tweetText']


#^^^for editing tweets



class DeteleteTweetView(DeleteView):
    model = Tweet
    template_name = 'delete_tweet.html'
    success_url = reverse_lazy('HomePage')