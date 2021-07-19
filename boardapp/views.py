from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BoardModel
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.db.models import Q


def signupfunc(request):
  if request.method == "POST":
    username = request.POST["username"]
    password = request.POST["password"]

    try:
      user = User.objects.create_user(username, '', password)
      return render(request, 'signup.html', {})
    except IntegrityError:
      return render(request, 'signup.html', {"error" : "このユーザーはすでに登録されています"})
  return render(request, "signup.html")


def loginfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("list")
    else:
        return render(request, 'login.html', {"context" : "ログインできませんでした"})
  return render(request, 'login.html', {"context" : "get method"})


def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, "list.html", {"object_list": object_list})


class BoardSearch(ListView):
  template_name = 'search.html'
  model = BoardModel
  def get_queryset(self):
    result = self.request.GET.get('query')

    if result:
      object_list = BoardModel.objects.filter(
        Q(title__icontains=result) | Q(author__icontains=result))
    else:
      object_list = BoardModel.objects.all()
    return object_list


def logoutfunc(request):
  logout(request)
  return redirect("login")


def detailfunc(request, pk):
  object = get_object_or_404(BoardModel, pk=pk)
  return render(request, 'detail.html', {'object': object})


def goodfunction(request, pk):
  object = BoardModel.objects.get(pk=pk)
  object.good = object.good + 1
  object.save()
  return redirect('list')


def readfunction(request, pk):
  object = BoardModel.objects.get(pk=pk)
  username = request.user.get_username()
  if username in object.readtext:
    return redirect('list')
  else:
    object.read = object.read + 1
    object.readtext = object.readtext + '' + username
    object.save()
    return redirect('list')


class BoardCreate(CreateView):
  template_name = 'create.html'
  model = BoardModel
  fields = ('title', 'content', 'author', 'snsimage')
  success_url = reverse_lazy('list')