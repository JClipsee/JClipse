from django.forms import ModelForm
from django import forms

from .models import Appointment
from .models import Offers
from .models import Client
from .models import Photographer


class AppointmentForm(ModelForm):
    offer = forms.ModelChoiceField(queryset=Offers.objects.all(), required=True)

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class PhotographerForm(ModelForm):
    class Meta:
        model = Photographer
        fields = '__all__'


class OfferForm(ModelForm):
    class Meta:
        model = Offers
        fields = '__all__'

