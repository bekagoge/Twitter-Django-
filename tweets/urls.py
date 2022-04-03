
from django.urls import path
from .views import HomePage, PostDetailView, AddTweetView, UpdateTweetView, DeteleteTweetView

urlpatterns = [
    #path('', views.detail, name='detail'),
    #path('', views.homepage, name="homepage"),
    path('', HomePage.as_view(), name='HomePage'),
    path('tweet/<int:pk>', PostDetailView.as_view(), name='PostDetails'),
    path('add_tweet/', AddTweetView.as_view(), name='add_tweet'),
    path('tweet/edit/<int:pk>', UpdateTweetView.as_view(), name='update_tweet'),
    path('tweet/<int:pk>/delete', DeteleteTweetView.as_view(), name='delete_tweet'),
  
]

# post/<int:pk> identifies each post with pk and gives each post uniqueness 


