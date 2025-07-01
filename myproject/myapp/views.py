from django.shortcuts import render
from .models import tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def tweet_list(request):
   Tweets=  tweet.objects.all().order_by('-created_at') 
   return render(request, 'tweet_list.html' ,{'tweets': Tweets}  )

@login_required
def create_tweet(request):
    if request.method == "POST" or None :
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
       
       
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})   
       


@login_required
def edit_tweet(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            updated_tweet = form.save(commit=False)
            updated_tweet.user = request.user
            updated_tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet_instance)

    return render(request, 'tweet_form.html', {'form': form})




def delete_tweet(request, tweet_id):
    tweet_instance = get_object_or_404(tweet, pk=tweet_id, user=request.user)

    if request.method == "POST":
        tweet_instance.delete()
        return redirect('tweet_list')

    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet_instance})

    
def register(request):
        if request.method =='POST':
           form = UserRegistrationForm(request.POST)
           if form.is_valid():
               user = form.save(commit=False)
               user.set_password(form.cleaned_data['password1'])
               user.save()
               login(request, user)
               return redirect('tweet_list')

           
        else:
            form = UserRegistrationForm()
             


        return render(request, 'registration/register.html', {'form': form})    
    