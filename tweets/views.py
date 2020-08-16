from django.shortcuts import render
#JsonResponse is for REST view
from django.http import HttpResponse, Http404, JsonResponse

#the dot indicates the same level directory
from .models import Tweet
from .forms import TweetForm

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, "pages/home.html", context={}, status=200)

def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = TweetForm()#empty form
    return render(request, 'components/form.html', context={'form': form})

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *arg, **kwargs):
    data = {
        "id": tweet_id
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "not found"
        status = 404
    return JsonResponse(data, status=status)
    #55:53
