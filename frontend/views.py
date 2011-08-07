# Create your views here.

from django.shortcuts import HttpResponse, render_to_response
from django.template.context import RequestContext
from expenses.models import Household

def homeView(request):
    """
    view for the homepage
    get all the households to display
    """
    return render_to_response('home.html',dict(households = Household.objects.all()), RequestContext(request))