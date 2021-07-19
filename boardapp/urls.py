from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunction, readfunction, BoardCreate, BoardSearch

urlpatterns = [
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('list/', listfunc, name="list"),
    path('logout/', logoutfunc, name="logout"),
    path('detail/<int:pk>', detailfunc, name="detail"),
    path('good/<int:pk>', goodfunction, name='good'),
    path('read/<int:pk>', readfunction, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
    path('search/', BoardSearch.as_view(), name="search")
]