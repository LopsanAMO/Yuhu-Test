from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from yuhutest.apps.users.forms import UserForm


class UserView(View):
    def get(self, request, *args, **kwargs):
        form = UserForm()
        context = {'form': form}
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            authenticated_user = authenticate(username=user_form.username, password=user_form.password)
            login(request, authenticated_user)
        return redirect('/tasks/')