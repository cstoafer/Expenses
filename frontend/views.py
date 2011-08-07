from django.views.generic.detail import DetailView
from expenses.models import Person, Household


class PersonView(DetailView):
    template_name = 'person/person_view.html'
    context_object_name = 'person'
    model = Person

class HouseholdView(DetailView):
    template_name = 'household/household_view.html'
    context_object_name = 'household'
    model = Household