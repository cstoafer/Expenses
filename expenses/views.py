# Create your views here.
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from expenses.utils import user_in_household
from models import Household, Transaction


class HouseholdTransactionsView(ListView):

    context_object_name = "transactions"
    template_name = "expenses/household_transactions.html"

    def get_queryset(self):
        return get_object_or_404(Household, pk = self.kwargs['pk']).transaction_set.order_by('-creation_date')


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HouseholdTransactionsView, self).get_context_data(**kwargs)
        household = get_object_or_404(Household, pk = self.kwargs['pk'])
        context['household'] = household
        #context['persons_ordered'] = (person for person in household.persons.order_by('id'))
        #context['mults_ordered'] = (transaction.multiplier_set.order_by('person') for transaction in context['transactions'])
        return context

    @method_decorator(user_in_household)
    def dispatch(self, *args, **kwargs):
        return super(HouseholdTransactionsView, self).dispatch(*args, **kwargs)