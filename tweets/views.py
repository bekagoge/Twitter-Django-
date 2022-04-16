#from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.http import HttpResponse, Http404
from .models import Tweet, Category
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

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all() 
        context = super(HomePage, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context
#^^^homepage view, puts tweets on main page

class PostDetailView(DetailView):
    model = Tweet
    template_name = 'postDetails.html'

#^^^tweets view, puts one tweet on page

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all() 
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


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




class AddCategoryView(CreateView):
    model = Category
    #form_class = TweetForm
    template_name = 'categoryPage.html'
    fields = '__all__'
    #fields = ('tweetTitle', tweetTitleTag', 'tweetAuthor', 'tweetText')




##function view, pass url with the name category from urls.py

def CategoryView(request, category):
    category_tweets= Tweet.objects.filter(tweetCategory = category.replace('-', ' '))
                                                                    #^^^doen't work 
    return render(request, 'categories.html', {'category': category.title().replace('-', ' '), 'category_tweets':category_tweets})

def CategoryListView(request):
    category_menu_list = Category.objects.all() 
                                                                    #^^^doen't work 
    return render(request, 'category_list.html', {category_menu_list})