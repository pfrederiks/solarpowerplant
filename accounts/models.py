from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _

FIRST_NAME_LABEL = _("First Name")
INITIALS_LABEL = _("Initials")
SURNAME_LABEL = _("Surname")
EMAIL_ADDRESS_LABEL = _("Email Address")
STREET_LABEL = _("Street")
NR_LABEL = _("Number")
SUFFIX_LABEL = _("Suffix")
ZIPCODE_LABEL = _("Zipcode")
CITY_LABEL = _("City")
KEEP_ME_UP_TO_DATE_LABEL = _("I would like to be receive project updates by e-mail:")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True)
    initials = models.CharField(max_length=20, blank=True)
    surname = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(null=True)
    street = models.CharField(max_length=100, blank=True)
    nr = models.IntegerField(null=True)
    suffix = models.CharField(max_length=10, blank=True)
    zipcode = models.CharField(max_length=8, blank=True)
    city = models.CharField(max_length=100, blank=True)
    keep_me_up_to_date = models.BooleanField()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(label=FIRST_NAME_LABEL, widget=forms.TextInput(attrs={'size': "15"}))
    surname = forms.CharField(label=SURNAME_LABEL, widget=forms.TextInput(attrs={'size': "25"}))
    initials = forms.CharField(label=INITIALS_LABEL, required=False, widget=forms.TextInput(attrs={'size': "10"}))
    email_address = forms.EmailField(label=EMAIL_ADDRESS_LABEL, widget=forms.TextInput(attrs={'size': "56"}))
    street = forms.CharField(label=STREET_LABEL, widget=forms.TextInput(attrs={'size': "30"}))
    nr = forms.IntegerField(label=NR_LABEL, widget=forms.TextInput(attrs={'size': "10"}))
    suffix = forms.CharField(label=SUFFIX_LABEL, required=False, widget=forms.TextInput(attrs={'size': "10"}))
    zipcode = forms.CharField(label=ZIPCODE_LABEL, widget=forms.TextInput(attrs={'size': "12"}))
    city = forms.CharField(label=CITY_LABEL, widget=forms.TextInput(attrs={'size': "41"}))
    keep_me_up_to_date = forms.BooleanField(label=KEEP_ME_UP_TO_DATE_LABEL, required=False)

    class Meta:
            model = Profile
            exclude = ('user',)
