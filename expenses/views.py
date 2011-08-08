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
        return Transaction.objects.filter(household=get_object_or_404(Household, pk = self.kwargs['pk']))


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HouseholdTransactionsView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['household'] = get_object_or_404(Household, pk = self.kwargs['pk'])
        return context

    @method_decorator(user_in_household)
    def dispatch(self, *args, **kwargs):
        return super(HouseholdTransactionsView, self).dispatch(*args, **kwargs)