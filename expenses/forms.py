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
    invited_user = forms.CharField(max_length=100, label='username', required=True)
    
    class Meta:
        model = Invited
        exclude = ('user',)
          
    def clean_invited_user(self):
        model = super(InviteToHouseholdForm, self).save(commit=False)
        check_user_exists = User.objects.filter(username__iexact=self.cleaned_data['invited_user'])
        check_user_in_household = Household.objects.filter(name__exact=self.cleaned_data['household'].name).filter(persons__user__username__iexact=self.cleaned_data['invited_user'])
        check_user_invited = Invited.objects.filter(household__name__exact=self.cleaned_data['household'].name).filter(user__username__iexact=self.cleaned_data['invited_user'])
        
        if not check_user_exists:
            raise forms.ValidationError("The username does not exist.")
        if check_user_in_household:
            msg_in_household = "This user is already part of this household."
            raise forms.ValidationError([msg_in_household])
        if check_user_invited:
            #existing_user = self.cleaned_data['invited_user']
            msg_invited = "This user has already been invited to this household"#{{ self.cleaned_data['household'] }}." #, self.cleaned_data['invited_user'], self.cleaned_data['household']
            raise forms.ValidationError([msg_invited])

        
        return self.cleaned_data['invited_user']
                
            
#    def clean(self):
#        check_user_exists = User.objects.filter(username__iexact=self.cleaned_data['invited_user'])
#        if not check_user_exists: #check_user_exists is None:
#            raise forms.ValidationError("The username does not exist.")
           
#        return self.cleaned_data
            
        
    def save(self, commit=True):
        m = super(InviteToHouseholdForm, self).save(commit=False)
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
