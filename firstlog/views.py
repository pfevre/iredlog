from django.shortcuts import render
from .models import Mailaddr

def mailaddress(request):
    return render(request, 'tutorial/people.html', {'mailaddress': Mailaddr.objects.all()})
# Create your views here.
