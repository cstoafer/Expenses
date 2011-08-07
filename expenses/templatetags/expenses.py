__author__ = 'jackdreilly'

from django import template
register = template.Library()


@register.inclusion_tag('expenses/household.html')
def render_household(household):
    """
    render html for a household
    in turn calls the render_person method for members
    """
    return dict(household = household)

@register.inclusion_tag('expenses/household_preview.html')
def render_household_pv(household):
    """
    render html for a household preview
    in turn calls the render_person method for members
    """
    return dict(household = household)



@register.inclusion_tag('expenses/person.html')
def render_person(person):
    """
    render html for a single person
    """
    return dict(person = person)

