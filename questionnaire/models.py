from django.db import models

from django.contrib.auth.models import User
from django import forms
from django.utils.translation import ugettext_lazy as _


MOTIVATION_LABEL = _("How did you get the idea to buy PV panels and install them?")
MOTIVATION = (
    (1, _("I want to solve World's energy crisis and/or prevent global warming")),
    (2, _("I want to make profit")),
    (3, _("Both")))

SOLAR_PANEL_YEARS_LABEL = _("How long have you owned a solar panel system?")
SOLAR_PANEL_YEARS = (
    (1, _("Less than 6 months")),
    (2, _("Between 6 months and 1 year")),
    (3, _("Between 1 year and 2 years")),
    (4, _("Between 2 and 5 years")),
    (5, _("More than 5 years")))

INSTALLED_CAPACITY_LABEL = _("How much capacity do you have currently installed?")
INSTALLED_CAPACITY = (
    (1, _("Less than 0,6 kW")),
    (2, _("Between 0,6 kW and 3.5 kW")),
    (3, _("Between 3.5 kW and 15 kW")),
    (4, _("More than 15 kW")))

FEED_IN_LABEL = _("Are you currently selling or have you ever sold electricity to the national grid since you have installed the solar panels?")
FEED_IN = (
    (True, _("Yes")),
    (False, _("No (skip the next question)")))

FEED_IN_KWH_LABEL = _("Could you give an estimate of the electrity in kWh you have sold last year (digits only)?")

SDE_SUPPORT_LABEL = _("Do you receive support from the SDE?")
SDE_SUPPORT = (
    (1, _("Yes")),
    (2, _("No")),
    (3, _("My application is still in process")))

MONITORING_LABEL = _("Do you currently have performance monitoring done on your PV system?")
MONITORING = (
    (1, _("I do it myself")),
    (2, _("I have external company doing this for me")),
    (3, _("I have no performance monitoring")))

METERING_EQUIPMENT_LABEL = _("What type of metering  equipment do you have?")
METERING_EQUIPMENT = (
    (1, _("Analog meter")),
    (2, _("Digital meter - with internet connection")),
    (3, _("Digital meter - without internet connection")))

METER_BRAND_AND_MODEL_LABEL = _("What is the brand and model of your metering equipment?\n Brand:")
MODEL_LABEL = _("Model:")

INVERTER_INTERNET_LABEL = _("Does your inverter have an internet function?")
INVERTER_INTERNET = (
    (1, _("Yes")),
    (2, _("No")),
    (3, _("I don't know")))

INTERNET_LABEL = _("What kind of internet connection do you have in your home?")
INTERNET = (
    (1, _("Dial-up (56k)")),
    (2, _("ISDN")),
    (3, _("Broadband (ADSL, fiber, cable)")),
    (4, _("Satellite internet")))

MALFUNCTION_LABEL = _("Did you ever experience any malfunctioning of the solar panels since installation?")
MALFUNCTION = (
    (True, _("Yes")),
    (False, _("No (Skip next 2 question)")))
		
DISCOVER_LABEL =  _("How did you discover that your system was not functioning well?")
DISCOVER = (
    (1, _("By regularly checking the meter")),
    (2, _("Through the electricity bill")),
    (3, _("By checking the display on the inverter")))

MAINTENANCE_LABEL = _("How many times did you have to call a maintenance firm to repair any malfunctioning of the system?")
# open box
MAINTENANCE_COSTS_LABEL = _("Could you give an estimate of your yearly maintenance costs?")

INTEREST_MONITORING_LABEL = _("Would you be interested in constant monitoring of the solar panels to optimize performance and reduce risk of lower yields?")
INTEREST_MONITORING = (
    (True, _("Yes")),
    (False, _("No")))


PARTICIPATION_LABEL = _("In the web-portal, together with other information, there will be tips on how to improve the efficiency of your PV system,"
                        "Do it yourself manuals, FAQ over most common malfunctions, recommended list of producers of latest, more efficient and"
                        "reliable PV equipment - would that stimulate you to participate?")
PARTICIPATION = (
    (True, _("Yes")),
    (False, _("No")))

PAY_FIXED_LABEL = _("How much would you be willing to pay per year (in euros) to be a member of the Virtual PV Plant? (digits only, decimals after a dot)")
PAY_PERCENTAGE_LABEL = _("Instead of a fixed amount, we could ask for a percentage of you yearly revenues selling electricity instead. What would you consider"
                         "a fair percentage? (digits only, decimals after a dot)")
PAY_PREFERENCE_LABEL = _("What would be your prefered pay option?")
PAY_PREFERENCE = (
    (1, _("Fixed Amount")),
    (2, _("Percentage of revenue")))

EXPLANATION_LABEL = _("What would be your motivation to join (or not to join) the virtual PV Plant?")

SPREAD_THE_WORD_LABEL = _("Would you be willing to spread the word to other PV panel owners of this system?")
SPREAD_THE_WORD = (
    (True, _("Yes")),
    (False, _("No")))


class Questions(models.Model):
    user = models.OneToOneField(User)
    motivation = models.IntegerField(null=True)
    solar_panel_years = models.IntegerField(null=True)
    installed_capacity = models.IntegerField(null=True)
    feed_in = models.NullBooleanField(null=True)
    feed_in_kwh = models.DecimalField(decimal_places=3, max_digits=20, null=True)
    sde_support = models.IntegerField(null=True)
    monitoring = models.IntegerField(null=True)
    metering_equipment = models.IntegerField(null=True)
    meter_brand = models.CharField(max_length=50, blank=True)
    meter_model = models.CharField(max_length=50, blank=True)
    inverter_internet = models.IntegerField(null=True)
    internet = models.IntegerField(null=True)
    malfunction = models.NullBooleanField(null=True)
    discover = models.IntegerField(null=True)
    maintenance = models.IntegerField(null=True)
    maintenance_costs = models.DecimalField(decimal_places=2, max_digits=20, null=True)
    interest_monitoring = models.NullBooleanField(null=True)
    participation = models.NullBooleanField(null=True)
    pay_fixed = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    pay_percentage = models.DecimalField(decimal_places=2, max_digits=4, null=True)
    pay_preference = models.IntegerField(null=True)
    explanation = models.CharField(max_length=3000, blank=True)
    spread_the_word = models.NullBooleanField(null=True)
    submission_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)


class QuestionsForm(forms.ModelForm):
    motivation = forms.ChoiceField(widget=forms.RadioSelect(),
                                   label=MOTIVATION_LABEL,
                                   choices=MOTIVATION)
    solar_panel_years = forms.ChoiceField(widget=forms.RadioSelect(),
                                          label=SOLAR_PANEL_YEARS_LABEL,
                                          choices=SOLAR_PANEL_YEARS)
    installed_capacity = forms.ChoiceField(widget=forms.RadioSelect(),
                                           label=INSTALLED_CAPACITY_LABEL,
                                           choices=INSTALLED_CAPACITY)
    feed_in = forms.ChoiceField(widget=forms.RadioSelect(),
                                label=FEED_IN_LABEL,
                                choices=FEED_IN)
    feed_in_kwh = forms.DecimalField(required=False,
                                     label=FEED_IN_KWH_LABEL,
                                     decimal_places=3, max_digits=20)
    sde_support = forms.ChoiceField(widget=forms.RadioSelect(),
                                    label=SDE_SUPPORT_LABEL,
                                    choices=SDE_SUPPORT)
    monitoring = forms.ChoiceField(widget=forms.RadioSelect(),
                                   label=MONITORING_LABEL,
                                   choices=MONITORING)
    metering_equipment = forms.ChoiceField(widget=forms.RadioSelect(),
                                           label=METERING_EQUIPMENT_LABEL,
                                           choices=METERING_EQUIPMENT)
    meter_brand = forms.CharField(label=METER_BRAND_AND_MODEL_LABEL)
    meter_model = forms.CharField(label=MODEL_LABEL)
    inverter_internet = forms.ChoiceField(widget=forms.RadioSelect(),
                                          label=INVERTER_INTERNET_LABEL,
                                          choices=INVERTER_INTERNET)
    internet = forms.ChoiceField(widget=forms.RadioSelect(),
                                 label=INTERNET_LABEL,
                                 choices=INTERNET)
    malfunction = forms.ChoiceField(required=False, widget=forms.RadioSelect(),
                                    label=MALFUNCTION_LABEL,
                                    choices=MALFUNCTION)
    discover = forms.ChoiceField(required=False, widget=forms.RadioSelect(),
                                 label=DISCOVER_LABEL,
                                 choices=DISCOVER)
    maintenance = forms.IntegerField(label=MAINTENANCE_LABEL, required=False)
    maintenance_costs = forms.DecimalField(label=MAINTENANCE_COSTS_LABEL,
                                           decimal_places=2, max_digits=20, required=False)
    interest_monitoring = forms.ChoiceField(widget=forms.RadioSelect(),
                                            label=INTEREST_MONITORING_LABEL,
                                            choices=INTEREST_MONITORING)
    participation = forms.ChoiceField(widget=forms.RadioSelect(),
                                      label=PARTICIPATION_LABEL,
                                      choices=PARTICIPATION)
    pay_fixed = forms.DecimalField(label=PAY_FIXED_LABEL, decimal_places=2, max_digits=5)
    pay_percentage = forms.DecimalField(label=PAY_PERCENTAGE_LABEL, decimal_places=2, max_digits=4)
    pay_preference = forms.ChoiceField(widget=forms.RadioSelect(),
                                       label=PAY_PREFERENCE_LABEL,
                                       choices=PAY_PREFERENCE)
    explanation = forms.CharField(required=False, label=EXPLANATION_LABEL,
                                  widget=forms.Textarea(attrs={'rows': "12", 'cols': "80"}))
    spread_the_word = forms.ChoiceField(widget=forms.RadioSelect(),
                                        label=SPREAD_THE_WORD_LABEL,
                                        choices=SPREAD_THE_WORD)

    class Meta():
            model = Questions
            exclude = ('user',)
