from django import forms
from django.forms.models import ModelForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from expenses.models import Transaction, Household, Person, Invited


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

    

class InviteToHouseholdForm(ModelForm):

    household = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Household.objects.all())
    invited_user = forms.CharField(max_length=100, label='username')
    
    class Meta:
        model = Invited
        exclude = ('user',)
    
    def save(self, commit=True):
# don't really get this, just copied it from stackoverflow
		m = super(InviteToHouseholdForm, self).save(commit=False)
		print self.cleaned_data['invited_user']
		m.user = User.objects.get(username=self.cleaned_data['invited_user'])
		if commit:
			m.save()
		
		return m
    
    

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
