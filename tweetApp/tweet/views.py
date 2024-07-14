from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm, UserRegistrationFrom
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(req):
    return render(req, 'index.html')

def tweet_list(req):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(req, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(req):
    if req.method == 'POST':
        form = TweetForm(req.POST, req.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(req, 'tweet_form.html', {'form':form})

@login_required
def tweet_edit(req,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=req.user)
    if req.method == 'POST':
        form = TweetForm(req.POST, req.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(req, 'tweet_form.html', {'form':form})

@login_required
def tweet_delete(req,tweet_id):
    tweet = get_object_or_404(Tweet,pk=tweet_id,user=req.user)
    if req.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(req, 'tweet_confirm_delete.html', {'tweet':tweet})

def register(req):
    if req.method == 'POST':
        form = UserRegistrationFrom(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(req, user)
            return redirect('tweet_list') 
    else:
        form = UserRegistrationFrom()

    return render(req, 'registration/register.html', {'form':form})

def search(req):
    query = req.GET.get('search')
    results = Tweet.objects.filter(text__icontains=query)
    return render(req, 'search.html', {'results': results, 'query': query,'results_count': results.count(),})
