from .models import dailystats, sprints
from django import forms

class sprintForm(forms.ModelForm):
    class Meta:
        model = sprints
        fields = ['latest_sprint']

class dailystatusForm(forms.ModelForm):
    class Meta:
        model = dailystats

        sprint = forms.ModelChoiceField(queryset=sprints.objects.all())
        story_id = forms.CharField(max_length=30)
        project = forms.CharField(max_length=30)
        Task = forms.CharField(max_length=500)
        Description = forms.CharField(max_length=5000)
        defects_filed = forms.CharField(max_length=30, required=False)
        defects_verified = forms.CharField(max_length=30, required=False)
        created_by = forms.CharField(max_length=20)

        # All the below list of fields should have data to submit. The corresponding fields should have validation in registration_form.html
        fields = ['sprint', 'story_id', 'project', 'Task', 'defects_filed', 'defects_verified', 'Description', 'created_by']

class updatedailystatusForm(forms.ModelForm):
    class Meta:
        model = dailystats

        widgets = {
            'story_id'          : forms.TextInput(attrs={'class': 'vTextField'}),
            'project'           : forms.TextInput(attrs={'class': 'vTextField'}),
            'Task'              : forms.TextInput(attrs={'class': 'vTextField'}),
            'Description'       : forms.Textarea(attrs={'class': 'vLargeTextField', 'maxlength':'5000'}),
            'defects_filed'     : forms.TextInput(attrs={'class': 'vTextField'}),
            'defects_verified'  : forms.TextInput(attrs={'class': 'vTextField'}),
            'created_by'        : forms.TextInput(attrs={'class': 'vTextField'})
        }

        fields = ['sprint', 'story_id', 'project', 'Task', 'defects_filed', 'defects_verified', 'Description','created_by']
