from django import forms
from django.forms.models import ModelForm
from django.shortcuts import get_object_or_404
from expenses.models import Transaction, Household, Person


class HouseholdTransactionForm(ModelForm):

    household = forms.ModelChoiceField(widget=forms.HiddenInput(),queryset=Household.objects.all())
    class Meta:
        model = Transaction

    def __init__(self,*args,**kwargs):
			super(HouseholdTransactionForm,self).__init__(*args, **kwargs)
                        if kwargs['instance']:
				persons = self.instance.household.persons
			elif self.initial.has_key('household'):
				persons  = self.initial['household'].persons
			else:
				persons = Person.objects.all()
			self.fields['transactor'].queryset = persons


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

class ProfileUpdateForm(ModelForm):
    first_name = forms.CharField('first name')
    last_name = forms.CharField('last name')
    email = forms.EmailField('e-mail address')
    class Meta:
        model = Person
        fields = ('name',)
    def __init__(self,*args,**kwargs):
        super(ProfileUpdateForm,self).__init__(*args, **kwargs)
        u = self.instance.user
        user_stuff = dict([('email', u.email), ('first_name', u.first_name), ('last_name', u.last_name)])
        self.initial.update(user_stuff)
    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(ProfileUpdateForm, self).save(commit=False)
        m.user.first_name = self.cleaned_data['first_name']
        m.user.last_name = self.cleaned_data['last_name']
        m.user.email = self.cleaned_data['email']
        if commit:
            m.save()
            m.user.save()
        return m
