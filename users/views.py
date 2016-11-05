from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .forms import UserInfoForm


class UserFormView(View):
    form_class = UserInfoForm
    template_name = 'name.html'

    def get(self, request, *args, **kwargs):
        """
        This will handle GET request.
        """
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        """
        This will handle POST request.
        """
        form = self.form_class(request.POST)
        if form.is_valid():
            # process form cleaned data
            form.save()
            request.session['username'] = form.data['username']
            return redirect('/hello',)

        return render(request, self.template_name, {'form': form})


class HelloView(View):
    template_name = 'hello.html'

    def get(self, request, *args, **kwargs):
        username = request.session.get('username', '')
        return render(request, self.template_name, {'username': username})
