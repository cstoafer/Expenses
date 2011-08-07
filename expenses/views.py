# Create your views here.

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from models import Household

def householdsView(request):
    return render_to_response('household.html', dict(household = Household.objects.order_by('?')[0]), RequestContext(request))