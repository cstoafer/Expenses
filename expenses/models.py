from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, unique=True)

    def get_absolute_url(self):
        return ('profiles_profile_detail', (), { 'username': self.user.username })
    get_absolute_url = models.permalink(get_absolute_url)

# Create your models here.

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()


class Household(models.Model):
    persons = models.ManyToManyField(Person)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return ', '.join(str(person) for person in self.persons.all())

class Transaction(models.Model):
    household = models.ForeignKey(Household)
    transactor = models.ForeignKey(Person)


    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        nMembers = self.household.persons.count()
        def_multipliers = 1./nMembers
        for person in self.household.persons.all():
            Multiplier(person= person, multiplier = def_multipliers, transaction = self).save()

    def __unicode__(self):
        return 'trans: %s, household: %i' % (self.transactor, self.household_id)

class Multiplier(models.Model):
    person = models.ForeignKey(Person)
    multiplier = models.FloatField()
    transaction = models.ForeignKey(Transaction)

    def __unicode__(self):
        return '%f - %s' % (self.multiplier, self.person)
