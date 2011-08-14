from django import forms
from django.forms.models import ModelForm
from django.shortcuts import get_object_or_404
from expenses.models import Transaction, Household, Person


class HouseholdTransactionForm(ModelForm):

    household = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Household.objects.all())
    class Meta:
        model = Transaction

    def __init__(self,*args,**kwargs):
		try:
			super(HouseholdTransactionForm,self).__init__(*args, **kwargs)
			if self.instance:
				persons = self.instance.household.persons
			elif self.initial.has_key('household'):
				persons  = self.initial['household'].persons
			else:
				persons = Person.objects.all()
			self.fields['transactor'].queryset = persons
		except:
			"you suck" 


class HouseholdCreateForm(ModelForm):
	class Meta:
		model = Household
		fields = ('name',)
	def save(self, force_insert=False, force_update=False, commit=True):
# don't really get this, just copied it from stackoverflow
		m = super(HouseholdCreateForm, self).save(commit=False)
		if commit:
			m.save()
		m.persons.add(self.initial['person'])
		return m
