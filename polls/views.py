from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .models import Poll, Option, User
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse

# Create your views here.


def poll_page(request, poll_pk):
    poll = Poll.objects.get(pk=poll_pk)
    if request.method ==  "POST":
        vote = request.POST["vote"]
        option = Option.objects.get(pk=vote)
        option.votes +=1
        option.save()
        return HttpResponseRedirect(reverse("index"))
    return render(request, "polls/poll_page.html", context={
        "poll": poll,
        "options": poll.poll_option.all().order_by("-votes")
    })


def add_poll(request, number_options):
    if request.method == "POST":
        for post, value in request.POST.items():
            if post == "csrfmiddlewaretoken":
                pass
            elif post == "title":
                poll = Poll.objects.create(title=value, owner=request.user)
                poll.save()
            else:    
                Option.objects.create(text=value, poll=poll)

        return HttpResponseRedirect(reverse("index"))
    # poll = Poll.objects.get(pk=poll_pk)
    for_range = range(1, int(number_options)+1)

    return render(request, "polls/add_poll.html", context={
        "range": for_range,
        "number_options": number_options,
    })


def index(request):
    if request.method =="POST":
        number_options = request.POST["number_options"]
        # poll = Poll.objects.create(number_options=number_options, owner=request.user)
        return HttpResponseRedirect(reverse("add_poll", args=(int(number_options), )))

    return render(request, "polls/index.html", context={
        "polls": Poll.objects.all().order_by("-poll_date"),
    })


# Authentication

def register_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if passw != confirmation:
            return render(request, "polls/register.html", context={
                "message": "Confirmação de senha incorreta!"
            })
        
        try:
            user = User.objects.create_user(username=user, password=passw)
            user.save()
        except IntegrityError:
            return render(request, "polls/register.html", context={
                "message": "Este email já está em uso.",
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    
    return render(request, "polls/register.html")

def login_view(request):
    if request.method == "POST":
        user = request.POST["username"]
        passw = request.POST["password"]
        user = authenticate(request, username=user, password=passw)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "polls/login.html", context={
                "message": "Email/Senha inválidos!"
            })
        
    return render(request, "polls/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))