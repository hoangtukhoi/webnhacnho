# from django import forms

# class ReminderForm(forms.Form):
#     date = forms.DateField(widget=forms.HiddenInput())
#     reminder = forms.CharField(label='Nhắc nhở', max_length=200)


from django import forms
from .models import Reminder
from .models import Diary

class ReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = ['date', 'reminder','time']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['diary']  # Chỉ hiển thị ô để viết nhật ký
        widgets = {
            'diary': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write your diary here...(Can not delete because it is your memories ^^)'}),
        }
        labels = {
            'diary': 'Your Diary',
        }