from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .views import View

# Create your views here.
class Home(View):
    def get(self, request, args, **kwargs):
         return render(request, 'profilelist.html')

method_decorator(login_required, name='dispatch')
class Profilelist(View):
    def get(self, request, args, **kwargs):
        profiles=request.user.profiles.all()
        return render(request, 'profilelist.html', {'profiles':profiles})
