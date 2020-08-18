from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse



def make_admin(request, user_id):
    if request.user.is_staff:
        user = User.objects.get(id=user_id)
        user.is_staff=True
        user.save()
    return HttpResponseRedirect(reverse("user-list"))

class UserList(generic.ListView):
    model = User
    template_name = 'user_list.html'
