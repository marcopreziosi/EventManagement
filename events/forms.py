from django import forms
from betterforms.multiform import MultiModelForm

from .models import Event, EventAgenda


class EventForm(forms.ModelForm):


    class Meta:
        model = Event
        fields = ['name', 'uid', 'description', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class EventAgendaForm(forms.ModelForm):


    class Meta:
        model = EventAgenda
        fields = ['start_time', 'end_time']

        widgets = {
            'start_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TextInput(attrs={'class': 'form-control', 'type': 'time'}),
        }


class EventCreateMultiForm(MultiModelForm):
    form_classes = {
        'event': EventForm,
        'event_agenda': EventAgendaForm,
    }