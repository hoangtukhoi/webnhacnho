# from django import forms

# class ReminderForm(forms.Form):
#     date = forms.DateField(widget=forms.HiddenInput())
#     reminder = forms.CharField(label='Nhắc nhở', max_length=200)


from django import forms
from .models import Reminder

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['date', 'reminder','time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
