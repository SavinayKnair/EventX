from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'event_name',
            'event_type',   # ✅ add this
            'event_date',
            'location',
            'description',
            'image'
        ]

        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
        }
